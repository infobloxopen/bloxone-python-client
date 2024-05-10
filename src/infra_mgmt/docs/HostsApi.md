# infra_mgmt.HostsApi

All URIs are relative to *http://csp.infoblox.com/api/infra/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AssignTags**](HostsApi.md#AssignTags) | **POST** /hosts/assign_tags | Assign tags for list of hosts.
[**Create**](HostsApi.md#Create) | **POST** /hosts | Create a Host resource.
[**Delete**](HostsApi.md#Delete) | **DELETE** /hosts/{id} | Delete a Host resource.
[**Disconnect**](HostsApi.md#Disconnect) | **POST** /hosts/{id}/disconnect | Disconnect a Host by resource ID.
[**List**](HostsApi.md#List) | **GET** /hosts | List all the Host resources for an account.
[**Read**](HostsApi.md#Read) | **GET** /hosts/{id} | Get a Host resource.
[**Replace**](HostsApi.md#Replace) | **POST** /hosts/{from.resource_id}/replace/{to.resource_id} | Migrate a Host&#39;s configuration from one to another.
[**UnassignTags**](HostsApi.md#UnassignTags) | **POST** /hosts/unassign_tags | Unassign tag for the list hosts.
[**Update**](HostsApi.md#Update) | **PUT** /hosts/{id} | Update a Host resource.


# **AssignTags**
> object AssignTags(body)

Assign tags for list of hosts.

Validation: - \"ids\" is required. - \"tags\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.models.assign_tags_request import AssignTagsRequest
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.HostsApi(api_client)
    body = infra_mgmt.AssignTagsRequest() # AssignTagsRequest | 

    try:
        # Assign tags for list of hosts.
        api_response = api_instance.AssignTags(body)
        print("The response of HostsApi->AssignTags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->AssignTags: %s\n" % e)
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

# **Create**
> CreateHostResponse Create(body)

Create a Host resource.

Validation: - \"display_name\" is required and should be unique.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.models.create_host_response import CreateHostResponse
from infra_mgmt.models.host import Host
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.HostsApi(api_client)
    body = infra_mgmt.Host() # Host | 

    try:
        # Create a Host resource.
        api_response = api_instance.Create(body)
        print("The response of HostsApi->Create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->Create: %s\n" % e)
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

# **Delete**
> Delete(id)

Delete a Host resource.

Validation: - \"id\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.HostsApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Delete a Host resource.
        api_instance.Delete(id)
    except Exception as e:
        print("Exception when calling HostsApi->Delete: %s\n" % e)
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

# **Disconnect**
> object Disconnect(id, body)

Disconnect a Host by resource ID.

The user can disconnect the host from the cloud (for example, if in case a host is compromised).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.models.disconnect_request import DisconnectRequest
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.HostsApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = infra_mgmt.DisconnectRequest() # DisconnectRequest | 

    try:
        # Disconnect a Host by resource ID.
        api_response = api_instance.Disconnect(id, body)
        print("The response of HostsApi->Disconnect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->Disconnect: %s\n" % e)
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

# **List**
> ListHostResponse List(filter=filter, order_by=order_by, offset=offset, limit=limit, page_token=page_token, fields=fields, tfilter=tfilter, torder_by=torder_by)

List all the Host resources for an account.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.models.list_host_response import ListHostResponse
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.HostsApi(api_client)
    filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)
    order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
    offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
    limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
    page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    tfilter = 'tfilter_example' # str | This parameter is used for filtering by tags. (optional)
    torder_by = 'torder_by_example' # str | This parameter is used for sorting by tags. (optional)

    try:
        # List all the Host resources for an account.
        api_response = api_instance.List(filter=filter, order_by=order_by, offset=offset, limit=limit, page_token=page_token, fields=fields, tfilter=tfilter, torder_by=torder_by)
        print("The response of HostsApi->List:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->List: %s\n" % e)
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

# **Read**
> GetHostResponse Read(id)

Get a Host resource.

Validation: - \"id\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.models.get_host_response import GetHostResponse
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.HostsApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Get a Host resource.
        api_response = api_instance.Read(id)
        print("The response of HostsApi->Read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->Read: %s\n" % e)
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

# **Replace**
> object Replace(from_resource_id, to_resource_id, body)

Migrate a Host's configuration from one to another.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.models.replace_host_request import ReplaceHostRequest
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.HostsApi(api_client)
    from_resource_id = 'from_resource_id_example' # str | An application specific resource identity of a resource
    to_resource_id = 'to_resource_id_example' # str | An application specific resource identity of a resource
    body = infra_mgmt.ReplaceHostRequest() # ReplaceHostRequest | 

    try:
        # Migrate a Host's configuration from one to another.
        api_response = api_instance.Replace(from_resource_id, to_resource_id, body)
        print("The response of HostsApi->Replace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->Replace: %s\n" % e)
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

# **UnassignTags**
> object UnassignTags(body)

Unassign tag for the list hosts.

Validation: - \"ids\" is required. - \"keys\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.models.unassign_tags_request import UnassignTagsRequest
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.HostsApi(api_client)
    body = infra_mgmt.UnassignTagsRequest() # UnassignTagsRequest | 

    try:
        # Unassign tag for the list hosts.
        api_response = api_instance.UnassignTags(body)
        print("The response of HostsApi->UnassignTags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->UnassignTags: %s\n" % e)
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

# **Update**
> UpdateHostResponse Update(id, body)

Update a Host resource.

Validation: - \"id\" is required. - \"display_name\" is required and should be unique. - \"pool_id\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.models.host import Host
from infra_mgmt.models.update_host_response import UpdateHostResponse
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.HostsApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = infra_mgmt.Host() # Host | 

    try:
        # Update a Host resource.
        api_response = api_instance.Update(id, body)
        print("The response of HostsApi->Update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->Update: %s\n" % e)
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
**201** | PUT operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

