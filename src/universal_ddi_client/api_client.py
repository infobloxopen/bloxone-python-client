# coding: utf-8
import abc
import datetime
from dateutil.parser import parse
from enum import Enum
import json
import mimetypes
import os
import re
import tempfile

from urllib.parse import quote
from typing import Tuple, Optional, List, Dict, Union
from pydantic import SecretStr

from universal_ddi_client.configuration import Configuration
from universal_ddi_client.api_response import ApiResponse, T as ApiResponseT
from universal_ddi_client.rest import RESTClientObject, RESTResponse
from universal_ddi_client.exceptions import (ApiValueError, ApiException,
                                       BadRequestException,
                                       UnauthorizedException,
                                       ForbiddenException, NotFoundException,
                                       ServiceException)

RequestSerialized = Tuple[str, str, Dict[str, str], Optional[str], List[str]]


HEADER_CLIENT = "x-infoblox-client"
HEADER_SDK = "x-infoblox-sdk"
SDK_IDENTIFIER = "python-sdk"

VERSION = 0.1

class ApiClient:
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    :param configuration: .Configuration object for this client
    """

    PRIMITIVE_TYPES = (float, bool, bytes, str, int)
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int,  # TODO remove as only py3 is supported?
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }
    _pool = None

    def __init__(
        self,
        configuration=None,
    ) -> None:
        # use default configuration if none is provided
        self._base_path = None
        if configuration is None:
            configuration = Configuration.get_default()
        self.configuration = configuration

        self.rest_client = RESTClientObject(configuration)
        self.default_headers = {}
        # Set default User-Agent.
        self.user_agent = f"universal-ddi-{SDK_IDENTIFIER}/{VERSION}"
        self.client_side_validation = configuration.client_side_validation

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    _default = None

    @classmethod
    def get_default(cls):
        """Return new instance of ApiClient.

        This method returns newly created, based on default constructor,
        object of ApiClient class or returns a copy of default
        ApiClient.

        :return: The ApiClient object.
        """
        if cls._default is None:
            cls._default = ApiClient()
        return cls._default

    @classmethod
    def set_default(cls, default):
        """Set default instance of ApiClient.

        It stores default ApiClient.

        :param default: object of ApiClient.
        """
        cls._default = default

    def call_api(self,
                 method,
                 url,
                 header_params=None,
                 body=None,
                 post_params=None,
                 _request_timeout=None) -> RESTResponse:
        """Makes the HTTP request (synchronous)
        :param method: Method to call.
        :param url: Path to method endpoint.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param _request_timeout: timeout setting for this request.
        :return: RESTResponse
        """

        try:
            # perform request and return response
            response_data = self.rest_client.request(
                method,
                url,
                headers=header_params,
                body=body,
                post_params=post_params,
                _request_timeout=_request_timeout)

        except ApiException as e:
            raise e

        return response_data

    def param_serialize(self,
                        method,
                        base_path,
                        resource_path,
                        path_params=None,
                        query_params=None,
                        header_params=None,
                        body=None,
                        post_params=None,
                        files=None,
                        auth_settings=None,
                        collection_formats=None,
                        _host=None,
                        _request_auth=None) -> RequestSerialized:
        """Builds the HTTP request params needed by the request.
        :param method: Method to call.
        :param base_path: Base path for the endpoint.
        :param resource_path: Path to method endpoint.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :return: tuple of form (path, http_method, query_params, header_params,
            body, post_params, files)
        """

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(
                self.parameters_to_tuples(header_params, collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params,
                                                    collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param))

        # post parameters
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params,
                                                    collection_formats)
            if files:
                post_params.extend(self.files_parameters(files))

        # auth setting
        self.update_params_for_auth(header_params, )

        # Update Client Name and SDK Identifier
        self.update_infoblox_headers(header_params)

        # body
        if body:
            body = self.add_default_tags(config,body)
            body = self.sanitize_for_serialization(body)

        # request url
        if _host is None:
            url = self.configuration.portal_url + base_path + resource_path
        else:
            # use server/host defined in path or operation instead
            url = _host + resource_path

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            url_query = self.parameters_to_url_query(query_params,
                                                     collection_formats)
            url += "?" + url_query

        return method, url, header_params, body, post_params

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is SecretStr, return obj.get_secret_value()
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is OpenAPI model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, SecretStr):
            return obj.get_secret_value()
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [
                self.sanitize_for_serialization(sub_obj) for sub_obj in obj
            ]
        elif isinstance(obj, tuple):
            return tuple(
                self.sanitize_for_serialization(sub_obj) for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        elif isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `openapi_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            if hasattr(obj, 'to_dict') and callable(getattr(obj, 'to_dict')):
                obj_dict = obj.to_dict()
            else:
                obj_dict = obj.__dict__

        return {
            key: self.sanitize_for_serialization(val)
            for key, val in obj_dict.items()
        }

    def response_deserialize(
        self,
        models,
        response_data: RESTResponse,
        response_types_map: Optional[Dict[str, ApiResponseT]] = None
    ) -> ApiResponse[ApiResponseT]:
        """Deserializes response into an object.
        :param models:
        :param response_data: RESTResponse object to be deserialized.
        :param response_types_map: dict of response types.
        :return: ApiResponse
        """

        msg = "RESTResponse.read() must be called before passing it to response_deserialize()"
        assert response_data.data is not None, msg

        response_type = response_types_map.get(str(response_data.status), None)
        if not response_type and isinstance(
                response_data.status,
                int) and 100 <= response_data.status <= 599:
            # if not found, look for '1XX', '2XX', etc.
            response_type = response_types_map.get(
                str(response_data.status)[0] + "XX", None)

        # deserialize response data
        response_text = None
        return_data = None
        try:
            if response_type == "bytearray":
                return_data = response_data.data
            elif response_type == "file":
                return_data = self.__deserialize_file(response_data)
            elif response_type is not None:
                match = None
                content_type = response_data.getheader('content-type')
                if content_type is not None:
                    match = re.search(r"charset=([a-zA-Z\-\d]+)[\s;]?",
                                      content_type)
                encoding = match.group(1) if match else "utf-8"
                response_text = response_data.data.decode(encoding)
                if response_type in ["bytearray", "str"]:
                    return_data = self.__deserialize_primitive(
                        response_text, response_type)
                else:
                    return_data = self.deserialize(models, response_text,
                                                   response_type)
        finally:
            if not 200 <= response_data.status <= 299:
                raise ApiException.from_response(
                    http_resp=response_data,
                    body=response_text,
                    data=return_data,
                )

        return ApiResponse(status_code=response_data.status,
                           data=return_data,
                           headers=response_data.getheaders(),
                           raw_data=response_data.data)

    def deserialize(self, models, response_text, response_type):
        """Deserializes response into an object.

        :param models:
        :param response_text: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """

        # fetch data from response object
        try:
            data = json.loads(response_text)
        except ValueError:
            data = response_text

        return self.__deserialize(models, data, response_type)

    def __deserialize(self, models, data, klass):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if isinstance(klass, str):
            if klass.startswith('List['):
                m = re.match(r'List\[(.*)]', klass)
                assert m is not None, "Malformed List type definition"
                sub_kls = m.group(1)
                return [
                    self.__deserialize(models, sub_data, sub_kls)
                    for sub_data in data
                ]

            if klass.startswith('Dict['):
                m = re.match(r'Dict\[([^,]*), (.*)]', klass)
                assert m is not None, "Malformed Dict type definition"
                sub_kls = m.group(2)
                return {
                    k: self.__deserialize(models, v, sub_kls)
                    for k, v in data.items()
                }

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datetime(data)
        elif issubclass(klass, Enum):
            return self.__deserialize_enum(data, klass)
        else:
            return self.__deserialize_model(data, klass)

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params: List[Tuple[str, str]] = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def parameters_to_url_query(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: URL query string (e.g. a=Hello%20World&b=123)
        """
        new_params: List[Tuple[str, str]] = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if isinstance(v, bool):
                v = str(v).lower()
            if isinstance(v, (int, float)):
                v = str(v)
            if isinstance(v, dict):
                v = json.dumps(v)

            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, str(value)) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(quote(str(value)) for value in v)))
            else:
                new_params.append((k, quote(str(v))))

        return "&".join(["=".join(map(str, item)) for item in new_params])

    def files_parameters(self, files: Dict[str, Union[str, bytes]]):
        """Builds form parameters.

        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []
        for k, v in files.items():
            if isinstance(v, str):
                with open(v, 'rb') as f:
                    filename = os.path.basename(f.name)
                    filedata = f.read()
            elif isinstance(v, bytes):
                filename = k
                filedata = v
            else:
                raise ValueError("Unsupported file value")
            mimetype = (mimetypes.guess_type(filename)[0]
                        or 'application/octet-stream')
            params.append(tuple([k, tuple([filename, filedata, mimetype])]))
        return params

    def select_header_accept(self, accepts: List[str]) -> Optional[str]:
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return None

        for accept in accepts:
            if re.search('json', accept, re.IGNORECASE):
                return accept

        return accepts[0]

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return None

        for content_type in content_types:
            if re.search('json', content_type, re.IGNORECASE):
                return content_type

        return content_types[0]

    def update_params_for_auth(
        self,
        headers,
    ) -> None:
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        """
        headers['Authorization'] = "Token {}".format(
            self.configuration.portal_key)

    def update_infoblox_headers(
            self,
            headers,
    )-> None:
        """Updates headers with client name and sdk identifier.

        :param headers: Header parameters dict to be updated.
        """
        headers[HEADER_CLIENT] = self.configuration.client_name
        headers[HEADER_SDK] = SDK_IDENTIFIER

    def __deserialize_file(self, response):
        """Deserializes body to file

        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        handle file downloading
        save response body into a tmp file and return the instance

        :param response:  RESTResponse.
        :return: file path.
        """
        fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            m = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                          content_disposition)
            assert m is not None, "Unexpected 'content-disposition' header value"
            filename = m.group(1)
            path = os.path.join(os.path.dirname(path), filename)

        with open(path, "wb") as f:
            f.write(response.data)

        return path

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return str(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return an original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise ApiException(
                status=0,
                reason="Failed to parse `{0}` as date object".format(string))

    def __deserialize_datetime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as datetime object".format(string)))

    def __deserialize_enum(self, data, klass):
        """Deserializes primitive type to enum.

        :param data: primitive type.
        :param klass: class literal.
        :return: enum value.
        """
        try:
            return klass(data)
        except ValueError:
            raise ApiException(status=0,
                               reason=("Failed to parse `{0}` as `{1}`".format(
                                   data, klass)))

    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        return klass.from_dict(data)

    def path_param_value(
        self,
        key: str,
        value: str,
        value_type: str = None,
    ):
        """Get the path parameter value, applying special formatting if needed.

        :param key: The key of the path parameter.
        :param value: The value of the path parameter to be converted to string.
        :param value_type: The type of the path parameter.
            If value_type is "resource_id", the value in the form of "app/type/id" or "type/id", the returned value will just have "id".
            If value type is "integer_id" ,the value in the form of an integer, the value will be returned as is.
        :return: The string representation of the path parameter.
        """
        if value_type == 'integer_id':
            return value

        if (key == 'id' and value_type is None) or value_type == 'resource_id':
            # Extract the last part of the resource id
            # e.g. "app/type/id" or "type/id" -> "id"
            # 'id' is considered as a resource_id by default
            split_value = value.split('/')
            if len(split_value) == 3 or len(split_value) == 2:
                return split_value[-1]

        return value

    def add_default_tags(
            self,
            configuration,
            body
    ):
        """Add default tags to the body if they are not already set.

        :param configuration: The configuration of the request.
        :param body: The body of the request.
        :return: The body with default tags added.
        """
        if len(configuration.default_tags) > 0 and hasattr(body, 'tags'):
            if body.tags is None:
                body.tags = {}
            for k, v in configuration.default_tags.items():
                if k not in body.tags:
                    body.tags[k] = v

        return body