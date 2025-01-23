# infra_mgmt.HostsApi

All URIs are relative to *http://csp.infoblox.com/api/infra/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_tags**](HostsApi.md#assign_tags) | **POST** /hosts/assign_tags | Assign tags for list of hosts.
[**create**](HostsApi.md#create) | **POST** /hosts | Create a Host resource.
[**delete**](HostsApi.md#delete) | **DELETE** /hosts/{id} | Delete a Host resource.
[**disconnect**](HostsApi.md#disconnect) | **POST** /hosts/{id}/disconnect | Disconnect a Host by resource ID.
[**list**](HostsApi.md#list) | **GET** /hosts | List all the Host resources for an account.
[**read**](HostsApi.md#read) | **GET** /hosts/{id} | Get a Host resource.
[**replace**](HostsApi.md#replace) | **POST** /hosts/{from.resource_id}/replace/{to.resource_id} | Migrate a Host&#39;s configuration from one to another.
[**unassign_tags**](HostsApi.md#unassign_tags) | **POST** /hosts/unassign_tags | Unassign tag for the list hosts.
[**update**](HostsApi.md#update) | **PUT** /hosts/{id} | Update a Host resource.


# **assign_tags**
> object assign_tags(body)

Assign tags for list of hosts.

Validation: - \"ids\" is required. - \"tags\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_mgmt

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
    api_instance = infra_mgmt.HostsApi(api_client)
    body = infra_mgmt.AssignTagsRequest() # AssignTagsRequest | 

    try:
        # Assign tags for list of hosts.
        api_response = api_instance.assign_tags(body)
        pprint("The response of HostsApi->assign_tags:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling HostsApi->assign_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignTagsRequest**](AssignTagsRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> CreateHostResponse create(body)

Create a Host resource.

Validation: - \"display_name\" is required and should be unique.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_mgmt

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
    api_instance = infra_mgmt.HostsApi(api_client)
    body = infra_mgmt.Host() # Host | 

    try:
        # Create a Host resource.
        api_response = api_instance.create(body)
        pprint("The response of HostsApi->create:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling HostsApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Host**](Host.md)|  | 

### Return type

[**CreateHostResponse**](CreateHostResponse.md)

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

Delete a Host resource.

Validation: - \"id\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_mgmt

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
    api_instance = infra_mgmt.HostsApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Delete a Host resource.
        api_instance.delete(id)
    except Exception as e:
        pprint("Exception when calling HostsApi->delete: %s\n" % e)
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

# **disconnect**
> object disconnect(id, body)

Disconnect a Host by resource ID.

The user can disconnect the host from the cloud (for example, if in case a host is compromised).

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_mgmt

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
    api_instance = infra_mgmt.HostsApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = infra_mgmt.DisconnectRequest() # DisconnectRequest | 

    try:
        # Disconnect a Host by resource ID.
        api_response = api_instance.disconnect(id, body)
        pprint("The response of HostsApi->disconnect:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling HostsApi->disconnect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**DisconnectRequest**](DisconnectRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListHostResponse list(filter=filter, order_by=order_by, offset=offset, limit=limit, page_token=page_token, fields=fields, tfilter=tfilter, torder_by=torder_by)

List all the Host resources for an account.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_mgmt

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
    api_instance = infra_mgmt.HostsApi(api_client)

    try:
        # List all the Host resources for an account.
        api_response = api_instance.list()
        pprint("The response of HostsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling HostsApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **tfilter** | **str**| This parameter is used for filtering by tags. | [optional] 
 **torder_by** | **str**| This parameter is used for sorting by tags. | [optional] 

### Return type

[**ListHostResponse**](ListHostResponse.md)

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
> GetHostResponse read(id)

Get a Host resource.

Validation: - \"id\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_mgmt

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
    api_instance = infra_mgmt.HostsApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Get a Host resource.
        api_response = api_instance.read(id)
        pprint("The response of HostsApi->read:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling HostsApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 

### Return type

[**GetHostResponse**](GetHostResponse.md)

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

# **replace**
> object replace(from_resource_id, to_resource_id, body)

Migrate a Host's configuration from one to another.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_mgmt

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
    api_instance = infra_mgmt.HostsApi(api_client)
    from_resource_id = 'from_resource_id_example' # str | An application specific resource identity of a resource
    to_resource_id = 'to_resource_id_example' # str | An application specific resource identity of a resource
    body = infra_mgmt.ReplaceHostRequest() # ReplaceHostRequest | 

    try:
        # Migrate a Host's configuration from one to another.
        api_response = api_instance.replace(from_resource_id, to_resource_id, body)
        pprint("The response of HostsApi->replace:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling HostsApi->replace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_resource_id** | **str**| An application specific resource identity of a resource | 
 **to_resource_id** | **str**| An application specific resource identity of a resource | 
 **body** | [**ReplaceHostRequest**](ReplaceHostRequest.md)|  | 

### Return type

**object**

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

# **unassign_tags**
> object unassign_tags(body)

Unassign tag for the list hosts.

Validation: - \"ids\" is required. - \"keys\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_mgmt

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
    api_instance = infra_mgmt.HostsApi(api_client)
    body = infra_mgmt.UnassignTagsRequest() # UnassignTagsRequest | 

    try:
        # Unassign tag for the list hosts.
        api_response = api_instance.unassign_tags(body)
        pprint("The response of HostsApi->unassign_tags:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling HostsApi->unassign_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnassignTagsRequest**](UnassignTagsRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> UpdateHostResponse update(id, body)

Update a Host resource.

Validation: - \"id\" is required. - \"display_name\" is required and should be unique. - \"pool_id\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_mgmt

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
    api_instance = infra_mgmt.HostsApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = infra_mgmt.Host() # Host | 

    try:
        # Update a Host resource.
        api_response = api_instance.update(id, body)
        pprint("The response of HostsApi->update:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling HostsApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**Host**](Host.md)|  | 

### Return type

[**UpdateHostResponse**](UpdateHostResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PUT operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

