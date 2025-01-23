# infra_provision.UIJoinTokenApi

All URIs are relative to *http://csp.infoblox.com/host-activation/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UIJoinTokenApi.md#create) | **POST** /jointoken | User can create a join token. Join token is random character string which is used for instant validation of new hosts.
[**delete**](UIJoinTokenApi.md#delete) | **DELETE** /jointoken/{id} | User can revoke the join token. Once revoked, it can not be used further. The join token record is preserved forever.
[**delete_set**](UIJoinTokenApi.md#delete_set) | **DELETE** /jointokens | User can revoke a list of join tokens. Once revoked, join tokens can not be used further. The records are preserved forever.
[**list**](UIJoinTokenApi.md#list) | **GET** /jointoken | User can list the join tokens for an account.
[**read**](UIJoinTokenApi.md#read) | **GET** /jointoken/{id} | User can get the join token providing its resource id in the parameter.
[**update**](UIJoinTokenApi.md#update) | **PATCH** /jointoken/{id} | User can modify the tags or expiration time of a join token.


# **create**
> CreateJoinTokenResponse create(body)

User can create a join token. Join token is random character string which is used for instant validation of new hosts.

Validation: - \"name\" is required and should be unique. - \"description\" is optioanl.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_provision

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UIJoinTokenApi(api_client)
    body = infra_provision.JoinToken() # JoinToken | 

    try:
        # User can create a join token. Join token is random character string which is used for instant validation of new hosts.
        api_response = api_instance.create(body)
        pprint("The response of UIJoinTokenApi->create:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UIJoinTokenApi->create: %s\n" % e)
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

# **delete**
> delete(id)

User can revoke the join token. Once revoked, it can not be used further. The join token record is preserved forever.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_provision

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UIJoinTokenApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # User can revoke the join token. Once revoked, it can not be used further. The join token record is preserved forever.
        api_instance.delete(id)
    except Exception as e:
        pprint("Exception when calling UIJoinTokenApi->delete: %s\n" % e)
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

# **delete_set**
> delete_set(body)

User can revoke a list of join tokens. Once revoked, join tokens can not be used further. The records are preserved forever.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_provision

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UIJoinTokenApi(api_client)
    body = infra_provision.DeleteJoinTokensRequest() # DeleteJoinTokensRequest | 

    try:
        # User can revoke a list of join tokens. Once revoked, join tokens can not be used further. The records are preserved forever.
        api_instance.delete_set(body)
    except Exception as e:
        pprint("Exception when calling UIJoinTokenApi->delete_set: %s\n" % e)
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

# **list**
> ListJoinTokenResponse list(filter=filter, order_by=order_by, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)

User can list the join tokens for an account.

Both active and revoked join tokens are listed by default.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_provision

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UIJoinTokenApi(api_client)

    try:
        # User can list the join tokens for an account.
        api_response = api_instance.list()
        pprint("The response of UIJoinTokenApi->list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UIJoinTokenApi->list: %s\n" % e)
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

# **read**
> ReadJoinTokenResponse read(id, fields=fields)

User can get the join token providing its resource id in the parameter.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_provision

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UIJoinTokenApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # User can get the join token providing its resource id in the parameter.
        api_response = api_instance.read(id)
        pprint("The response of UIJoinTokenApi->read:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UIJoinTokenApi->read: %s\n" % e)
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

# **update**
> UpdateJoinTokenResponse update(id, body)

User can modify the tags or expiration time of a join token.

Validation: Following fields is needed. Provide what needs to be - \"expires_at\" - \"tags\"

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_provision

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UIJoinTokenApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = infra_provision.JoinToken() # JoinToken | 

    try:
        # User can modify the tags or expiration time of a join token.
        api_response = api_instance.update(id, body)
        pprint("The response of UIJoinTokenApi->update:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UIJoinTokenApi->update: %s\n" % e)
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

