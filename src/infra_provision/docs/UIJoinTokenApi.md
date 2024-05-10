# infra_provision.UIJoinTokenApi

All URIs are relative to *http://csp.infoblox.com/host-activation/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Create**](UIJoinTokenApi.md#Create) | **POST** /jointoken | User can create a join token. Join token is random character string which is used for instant validation of new hosts.
[**Delete**](UIJoinTokenApi.md#Delete) | **DELETE** /jointoken/{id} | User can revoke the join token. Once revoked, it can not be used further. The join token record is preserved forever.
[**DeleteSet**](UIJoinTokenApi.md#DeleteSet) | **DELETE** /jointokens | User can revoke a list of join tokens. Once revoked, join tokens can not be used further. The records are preserved forever.
[**List**](UIJoinTokenApi.md#List) | **GET** /jointoken | User can list the join tokens for an account.
[**Read**](UIJoinTokenApi.md#Read) | **GET** /jointoken/{id} | User can get the join token providing its resource id in the parameter.
[**Update**](UIJoinTokenApi.md#Update) | **PATCH** /jointoken/{id} | User can modify the tags or expiration time of a join token.


# **Create**
> CreateJoinTokenResponse Create(body)

User can create a join token. Join token is random character string which is used for instant validation of new hosts.

Validation: - \"name\" is required and should be unique. - \"description\" is optioanl.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_provision
from infra_provision.models.create_join_token_response import CreateJoinTokenResponse
from infra_provision.models.join_token import JoinToken
from infra_provision.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/host-activation/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_provision.Configuration(
    host = "http://csp.infoblox.com/host-activation/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with infra_provision.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UIJoinTokenApi(api_client)
    body = infra_provision.JoinToken() # JoinToken | 

    try:
        # User can create a join token. Join token is random character string which is used for instant validation of new hosts.
        api_response = api_instance.Create(body)
        print("The response of UIJoinTokenApi->Create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIJoinTokenApi->Create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JoinToken**](JoinToken.md)|  | 

### Return type

[**CreateJoinTokenResponse**](CreateJoinTokenResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Delete**
> Delete(id)

User can revoke the join token. Once revoked, it can not be used further. The join token record is preserved forever.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_provision
from infra_provision.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/host-activation/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_provision.Configuration(
    host = "http://csp.infoblox.com/host-activation/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with infra_provision.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UIJoinTokenApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # User can revoke the join token. Once revoked, it can not be used further. The join token record is preserved forever.
        api_instance.Delete(id)
    except Exception as e:
        print("Exception when calling UIJoinTokenApi->Delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteSet**
> DeleteSet(body)

User can revoke a list of join tokens. Once revoked, join tokens can not be used further. The records are preserved forever.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_provision
from infra_provision.models.delete_join_tokens_request import DeleteJoinTokensRequest
from infra_provision.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/host-activation/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_provision.Configuration(
    host = "http://csp.infoblox.com/host-activation/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with infra_provision.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UIJoinTokenApi(api_client)
    body = infra_provision.DeleteJoinTokensRequest() # DeleteJoinTokensRequest | 

    try:
        # User can revoke a list of join tokens. Once revoked, join tokens can not be used further. The records are preserved forever.
        api_instance.DeleteSet(body)
    except Exception as e:
        print("Exception when calling UIJoinTokenApi->DeleteSet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteJoinTokensRequest**](DeleteJoinTokensRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **List**
> ListJoinTokenResponse List(filter=filter, order_by=order_by, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)

User can list the join tokens for an account.

Both active and revoked join tokens are listed by default.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_provision
from infra_provision.models.list_join_token_response import ListJoinTokenResponse
from infra_provision.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/host-activation/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_provision.Configuration(
    host = "http://csp.infoblox.com/host-activation/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with infra_provision.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UIJoinTokenApi(api_client)
    filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)
    order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
    offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
    limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
    page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
    tfilter = 'tfilter_example' # str | This parameter is used for filtering by tags. (optional)
    torder_by = 'torder_by_example' # str | This parameter is used for sorting by tags. (optional)

    try:
        # User can list the join tokens for an account.
        api_response = api_instance.List(filter=filter, order_by=order_by, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)
        print("The response of UIJoinTokenApi->List:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIJoinTokenApi->List: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **tfilter** | **str**| This parameter is used for filtering by tags. | [optional] 
 **torder_by** | **str**| This parameter is used for sorting by tags. | [optional] 

### Return type

[**ListJoinTokenResponse**](ListJoinTokenResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Read**
> ReadJoinTokenResponse Read(id, fields=fields)

User can get the join token providing its resource id in the parameter.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_provision
from infra_provision.models.read_join_token_response import ReadJoinTokenResponse
from infra_provision.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/host-activation/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_provision.Configuration(
    host = "http://csp.infoblox.com/host-activation/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with infra_provision.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UIJoinTokenApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

    try:
        # User can get the join token providing its resource id in the parameter.
        api_response = api_instance.Read(id, fields=fields)
        print("The response of UIJoinTokenApi->Read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIJoinTokenApi->Read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**ReadJoinTokenResponse**](ReadJoinTokenResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Update**
> UpdateJoinTokenResponse Update(id, body)

User can modify the tags or expiration time of a join token.

Validation: Following fields is needed. Provide what needs to be - \"expires_at\" - \"tags\"

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_provision
from infra_provision.models.join_token import JoinToken
from infra_provision.models.update_join_token_response import UpdateJoinTokenResponse
from infra_provision.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/host-activation/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_provision.Configuration(
    host = "http://csp.infoblox.com/host-activation/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with infra_provision.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UIJoinTokenApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = infra_provision.JoinToken() # JoinToken | 

    try:
        # User can modify the tags or expiration time of a join token.
        api_response = api_instance.Update(id, body)
        print("The response of UIJoinTokenApi->Update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIJoinTokenApi->Update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**JoinToken**](JoinToken.md)|  | 

### Return type

[**UpdateJoinTokenResponse**](UpdateJoinTokenResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PATCH operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

