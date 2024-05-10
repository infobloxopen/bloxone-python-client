# fw.NetworkListsApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateNetworkList**](NetworkListsApi.md#CreateNetworkList) | **POST** /network_lists | Create Network List.
[**DeleteNetworkLists**](NetworkListsApi.md#DeleteNetworkLists) | **DELETE** /network_lists | Delete Network Lists.
[**DeleteSingleNetworkLists**](NetworkListsApi.md#DeleteSingleNetworkLists) | **DELETE** /network_lists/{id} | Delete Network Lists.
[**ListNetworkLists**](NetworkListsApi.md#ListNetworkLists) | **GET** /network_lists | List Network Lists.
[**ReadNetworkList**](NetworkListsApi.md#ReadNetworkList) | **GET** /network_lists/{id} | Read Network List.
[**UpdateNetworkList**](NetworkListsApi.md#UpdateNetworkList) | **PUT** /network_lists/{id} | Update Network List.


# **CreateNetworkList**
> NetworkListCreateResponse CreateNetworkList(body)

Create Network List.

Use this method to create a Network List object.  Before you can apply security policies, you must first define the networks that you want to protect from malicious attacks. The first step in configuring BloxOne Cloud is to set up DNS Firewall by defining your remote networks. You identify these external networks by their IP addresses. A network can contain a group of IPv4 or IPv6 addresses or blocks.  Required: - name - items 

### Example


```python
import fw
from fw.models.network_list import NetworkList
from fw.models.network_list_create_response import NetworkListCreateResponse
from fw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fw.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with fw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.NetworkListsApi(api_client)
    body = fw.NetworkList() # NetworkList | The Network List object.

    try:
        # Create Network List.
        api_response = api_instance.CreateNetworkList(body)
        print("The response of NetworkListsApi->CreateNetworkList:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkListsApi->CreateNetworkList: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkList**](NetworkList.md)| The Network List object. | 

### Return type

[**NetworkListCreateResponse**](NetworkListCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;name&#39; value cannot be equal to &#39;All BloxOne Endpoints (Default)&#39;, &#39;All Networks (Default)&#39;, &#39;All DNS Forwarder Proxies (Default)&#39; - &#39;description&#39; length cannot exceed 256 characters limit - &#39;items&#39; value must not be empty - &#39;items&#39; value must contain valid CIDRs from range [24, 32] - CIDRs in &#39;items&#39; cannot overlap with each other and with existing items for all accounts |  -  |
**409** |  - &#39;name&#39; value must be unique among network lists belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteNetworkLists**
> DeleteNetworkLists(body)

Delete Network Lists.

Use this method to delete the Network List objects. Deletion of multiple lists is an all-or-nothing operation (if any of the specified lists can not be deleted then none of the specified lists will be deleted).  Before you can apply security policies, you must first define the networks that you want to protect from malicious attacks. The first step in configuring BloxOne Cloud is to set up DNS Firewall by defining your remote networks. You identify these external networks by their IP addresses. A network can contain a group of  or IPv6 addresses or blocks.  Required: - ids 

### Example


```python
import fw
from fw.models.network_lists_delete_request import NetworkListsDeleteRequest
from fw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fw.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with fw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.NetworkListsApi(api_client)
    body = fw.NetworkListsDeleteRequest() # NetworkListsDeleteRequest | 

    try:
        # Delete Network Lists.
        api_instance.DeleteNetworkLists(body)
    except Exception as e:
        print("Exception when calling NetworkListsApi->DeleteNetworkLists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkListsDeleteRequest**](NetworkListsDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** |  - &#39;ids&#39; value must be non-empty - &#39;ids&#39; value must contain unique elements - &#39;ids&#39; value must contain values that are greater than or equal to zero - network list that is assigned to a security policy cannot be deleted |  -  |
**404** |  - &#39;ids&#39; value must contain existing network list identifiers |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteSingleNetworkLists**
> DeleteSingleNetworkLists(id)

Delete Network Lists.

Use this method to delete the Network List object by the specified Network List object id.  Before you can apply security policies, you must first define the networks that you want to protect from malicious attacks. The first step in configuring BloxOne Cloud is to set up DNS Firewall by defining your remote networks. You identify these external networks by their IP addresses. A network can contain a group of  or IPv6 addresses or blocks.  

### Example


```python
import fw
from fw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fw.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with fw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.NetworkListsApi(api_client)
    id = 56 # int | The Network List object identifier.

    try:
        # Delete Network Lists.
        api_instance.DeleteSingleNetworkLists(id)
    except Exception as e:
        print("Exception when calling NetworkListsApi->DeleteSingleNetworkLists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Network List object identifier. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** |  - \&quot;invalid &#39;id&#39;: value must be greater than or equal to 0\&quot; - network list that is assigned to a security policy cannot be deleted |  -  |
**404** |  - &#39;id&#39; value must contain existing network list identifiers |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListNetworkLists**
> NetworkListMultiResponse ListNetworkLists(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token)

List Network Lists.

Use this method to retrieve information on all Network List objects for the account.  Before you can apply security policies, you must first define the networks that you want to protect from malicious attacks. The first step in configuring BloxOne Cloud is to set up DNS Firewall by defining your remote networks. You identify these external networks by their IP addresses. A network can contain a group of IPv4 or IPv6 addresses or blocks.  

### Example


```python
import fw
from fw.models.network_list_multi_response import NetworkListMultiResponse
from fw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fw.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with fw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.NetworkListsApi(api_client)
    filter = 'filter_example' # str | A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name                    | type   | Supported Op                | | ----------------------- | ------ | --------------------------- | | id                      | int32  | !=, ==, >, <, <=, >=        | | policy_id               | int32  | !=, ==, >, <, <=, >=        | | name                    | string | !=, ==, ~, !~, >, <, <=, >= | | description             | string | !=, ==, ~, !~, >, <, <=, >= | | default_security_policy | bool   | !=, ==                      | | items                   | string | >=                           |  In addition grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Groupping Operators  |  Allowed sets of parameters that can be groupped in one query:  - id, policy_id, name, description, default_security_policy - items  Example: ``` ?_filter=\"((name=='net_list1')or(name~'list_b'))and(default_security_policy!='true')\" ```  (optional)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
    limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
    page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)

    try:
        # List Network Lists.
        api_response = api_instance.ListNetworkLists(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token)
        print("The response of NetworkListsApi->ListNetworkLists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkListsApi->ListNetworkLists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;.  You can filter by following fields:  | Name                    | type   | Supported Op                | | ----------------------- | ------ | --------------------------- | | id                      | int32  | !&#x3D;, &#x3D;&#x3D;, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D;        | | policy_id               | int32  | !&#x3D;, &#x3D;&#x3D;, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D;        | | name                    | string | !&#x3D;, &#x3D;&#x3D;, ~, !~, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D; | | description             | string | !&#x3D;, &#x3D;&#x3D;, ~, !~, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D; | | default_security_policy | bool   | !&#x3D;, &#x3D;&#x3D;                      | | items                   | string | &gt;&#x3D;                           |  In addition grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Groupping Operators  |  Allowed sets of parameters that can be groupped in one query:  - id, policy_id, name, description, default_security_policy - items  Example: &#x60;&#x60;&#x60; ?_filter&#x3D;\&quot;((name&#x3D;&#x3D;&#39;net_list1&#39;)or(name~&#39;list_b&#39;))and(default_security_policy!&#x3D;&#39;true&#39;)\&quot; &#x60;&#x60;&#x60;  | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 

### Return type

[**NetworkListMultiResponse**](NetworkListMultiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ReadNetworkList**
> NetworkListReadResponse ReadNetworkList(id, fields=fields, name=name)

Read Network List.

Use this method to retrieve information on the specified Network List object.  Before you can apply security policies, you must first define the networks that you want to protect from malicious attacks. The first step in configuring BloxOne Cloud is to set up DNS Firewall by defining your remote networks. You identify these external networks by their IP addresses. A network can contain a group of IPv4 or IPv6 addresses or blocks. 

### Example


```python
import fw
from fw.models.network_list_read_response import NetworkListReadResponse
from fw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fw.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with fw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.NetworkListsApi(api_client)
    id = 56 # int | The Network List object identifier.
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    name = 'name_example' # str | The name of the network list. (optional)

    try:
        # Read Network List.
        api_response = api_instance.ReadNetworkList(id, fields=fields, name=name)
        print("The response of NetworkListsApi->ReadNetworkList:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkListsApi->ReadNetworkList: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Network List object identifier. | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **name** | **str**| The name of the network list. | [optional] 

### Return type

[**NetworkListReadResponse**](NetworkListReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |
**404** |  - &#39;id&#39; value must contain existing network list identifier |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateNetworkList**
> NetworkListUpdateResponse UpdateNetworkList(id, body)

Update Network List.

Use this method to update a specified Network List object.  Before you can apply security policies, you must first define the networks that you want to protect from malicious attacks. The first step in configuring BloxOne Cloud is to set up DNS Firewall by defining your remote networks. You identify these external networks by their IP addresses. A network can contain a group of IPv4 or IPv6 addresses or blocks.  Required: - name - items 

### Example


```python
import fw
from fw.models.network_list import NetworkList
from fw.models.network_list_update_response import NetworkListUpdateResponse
from fw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fw.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with fw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.NetworkListsApi(api_client)
    id = 56 # int | The Network List object identifier.
    body = fw.NetworkList() # NetworkList | The Network List object.

    try:
        # Update Network List.
        api_response = api_instance.UpdateNetworkList(id, body)
        print("The response of NetworkListsApi->UpdateNetworkList:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkListsApi->UpdateNetworkList: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Network List object identifier. | 
 **body** | [**NetworkList**](NetworkList.md)| The Network List object. | 

### Return type

[**NetworkListUpdateResponse**](NetworkListUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PUT operation response |  -  |
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;name&#39; value cannot be equal to &#39;All BloxOne Endpoints (Default)&#39;, &#39;All Networks (Default)&#39;, &#39;All DNS Forwarder Proxies (Default)&#39; - &#39;description&#39; length cannot exceed 256 characters limit - &#39;items&#39; value must not be empty - &#39;items&#39; value must contain valid CIDRs from range [24, 32] - CIDRs in &#39;items&#39; cannot overlap with each other and with existing items for all accounts |  -  |
**404** |  - &#39;id&#39; value must contain existing network list identifier |  -  |
**409** |  - &#39;name&#39; value must be unique among network lists belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

