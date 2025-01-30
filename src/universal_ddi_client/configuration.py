# coding: utf-8

import os
import copy
import logging
from logging import FileHandler
import multiprocessing
import sys
from typing import Optional

import http.client as httplib

JSON_SCHEMA_VALIDATION_KEYWORDS = {
    'multipleOf', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum',
    'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems'
}

class Configuration:
    """This class contains various settings of the API client.

    :param portal_url: URL for Infoblox Cloud Services Portal.
      Can also be configured using the `INFOBLOX_PORTAL_URL` environment variable.
      Default is `https://csp.infoblox.com`.
    :param portal_key: API Key for accessing the Infoblox API.
      Can also be configured by using the `INFOBLOX_PORTAL_KEY` environment variable.

      You can configure an API key for your user account in the Infoblox Cloud Services Portal.
      Please refer to the following link for more information: https://docs.infoblox.com/space/BloxOneCloud/35430405/Configuring+User+API+Keys.
    :param client_name: The name of the client using the API.
      This can be used to identify the client in the logs.
      If not provided, the client name will be set to `universal-ddi-python-client`.
    :param ssl_ca_cert: str - the path to a file of concatenated CA certificates
      in PEM format.

    :Example:

    API Key Authentication Example.
conf = ipam.Configuration(
    portal_key='your_portal_key'
)

    The following header will be added to the HTTP request:
       Authorization: Token your_portal_key
    """

    _default = None

    def __init__(
        self,
        portal_url=None,
        portal_key=None,
        client_name=None,
        ssl_ca_cert=None,
    ) -> None:
        """Constructor
        """

        self.portal_url = portal_url or os.getenv("INFOBLOX_PORTAL_URL") or os.getenv("BLOXONE_CSP_URL") or "https://csp.infoblox.com"
        """Default CSP url
        """
        self.temp_folder_path = None
        """Temp file folder for downloading files
        """
        # Authentication Settings
        self.portal_key = os.getenv('INFOBLOX_PORTAL_KEY') or os.getenv('BLOXONE_API_KEY') or ""
        if portal_key:
            self.portal_key = portal_key
        """API Key
        """
        self.client_name = "universal-ddi-python-client" if client_name is None else client_name
        """Default Client name
        """
        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("ipam")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler: Optional[FileHandler] = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        self.debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = ssl_ca_cert
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """
        self.tls_server_name = None
        """SSL/TLS Server Name Indication (SNI)
           Set this to the SNI value expected by the server.
        """

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        """urllib3 connection pool's maximum number of connections saved
           per pool. urllib3 uses 1 connection as default value, but this is
           not the best value when you are making a lot of possibly parallel
           requests to the same host, which is often the case here.
           cpu_count * 5 is used as default value to increase performance.
        """

        self.proxy: Optional[str] = None
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = None
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        self.socket_options = None
        """Options to pass down to the underlying urllib3 socket
        """

        self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        """datetime format
        """

        self.date_format = "%Y-%m-%d"
        """date format
        """

        self.default_tags = {}
        """Default tags
        """

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    @classmethod
    def set_default(cls, default):
        """Set default instance of configuration.

        It stores default configuration, which can be
        returned by get_default_copy method.

        :param default: object of Configuration
        """
        cls._default = default

    @classmethod
    def get_default(cls):
        """Return the default configuration.

        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration.

        :return: The configuration object.
        """
        if cls._default is None:
            cls._default = Configuration()
        return cls._default

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :return: The logger file path.
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :return: The debug status, True or False.
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :return: The format string.
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: v1\n"\
               "SDK Package Version: 0.1.0".\
               format(env=sys.platform, pyversion=sys.version)

    @property
    def portal_url(self):
        """Get the CSP URL.

        :return: The CSP URL.
        """
        return self.__portal_url

    @portal_url.setter
    def portal_url(self, value):
        """Set the CSP URL.

        :param value: The CSP URL.
        """
        self.__portal_url = value

    @property
    def portal_key(self):
        """Get the API key.

        :return: The API key.
        """
        return self.__portal_key

    @portal_key.setter
    def portal_key(self, value):
        """Set the API key.

        :param value: The API key.
        """
        self.__portal_key = value

    @property
    def client_name(self):
        """Get the client name.

        :return: The client name.
        """
        return self.__client_name

    @client_name.setter
    def client_name(self, value):
        """Set the client name.

        :param value: The client name.
        """
        self.__client_name = value

    @property
    def default_tags(self):
        """Get the default tags.

        :return: The default tags.
        """
        return self.__default_tags

    @default_tags.setter
    def default_tags(self, value):
        """Set the default tags.

        :param value: The default tags.
        """
        self.__default_tags = value
