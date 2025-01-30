# fw.NetworkListsApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_list**](NetworkListsApi.md#create_network_list) | **POST** /network_lists | Create Network List.
[**delete_network_lists**](NetworkListsApi.md#delete_network_lists) | **DELETE** /network_lists | Delete Network Lists.
[**delete_single_network_lists**](NetworkListsApi.md#delete_single_network_lists) | **DELETE** /network_lists/{id} | Delete Network Lists.
[**list_network_lists**](NetworkListsApi.md#list_network_lists) | **GET** /network_lists | List Network Lists.
[**read_network_list**](NetworkListsApi.md#read_network_list) | **GET** /network_lists/{id} | Read Network List.
[**update_network_list**](NetworkListsApi.md#update_network_list) | **PUT** /network_lists/{id} | Update Network List.


# **create_network_list**
> NetworkListCreateResponse create_network_list(body)

Create Network List.

Use this method to create a Network List object.  Before you can apply security policies, you must first define the networks that you want to protect from malicious attacks. The first step in configuring Infoblox Cloud is to set up DNS Firewall by defining your remote networks. You identify these external networks by their IP addresses. A network can contain a group of IPv4 or IPv6 addresses or blocks.  Required: - name - items 

### Example

```python
import os
from pprint import pprint

import fw

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.NetworkListsApi(api_client)
    body = fw.NetworkList() # NetworkList | The Network List object.

    try:
        # Create Network List.
        api_response = api_instance.create_network_list(body)
        pprint("The response of NetworkListsApi->create_network_list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling NetworkListsApi->create_network_list: %s\n" % e)
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
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;name&#39; value cannot be equal to &#39;All Infoblox Endpoints (Default)&#39;, &#39;All Networks (Default)&#39;, &#39;All DNS Forwarder Proxies (Default)&#39; - &#39;description&#39; length cannot exceed 256 characters limit - &#39;items&#39; value must not be empty - &#39;items&#39; value must contain valid CIDRs from range [24, 32] - CIDRs in &#39;items&#39; cannot overlap with each other and with existing items for all accounts |  -  |
**409** |  - &#39;name&#39; value must be unique among network lists belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_lists**
> delete_network_lists(body)

Delete Network Lists.

Use this method to delete the Network List objects. Deletion of multiple lists is an all-or-nothing operation (if any of the specified lists can not be deleted then none of the specified lists will be deleted).  Before you can apply security policies, you must first define the networks that you want to protect from malicious attacks. The first step in configuring Infoblox Cloud is to set up DNS Firewall by defining your remote networks. You identify these external networks by their IP addresses. A network can contain a group of  or IPv6 addresses or blocks.  Required: - ids 

### Example

```python
import os
from pprint import pprint

import fw

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.NetworkListsApi(api_client)
    body = fw.NetworkListsDeleteRequest() # NetworkListsDeleteRequest | 

    try:
        # Delete Network Lists.
        api_instance.delete_network_lists(body)
    except Exception as e:
        pprint("Exception when calling NetworkListsApi->delete_network_lists: %s\n" % e)
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

# **delete_single_network_lists**
> delete_single_network_lists(id)

Delete Network Lists.

Use this method to delete the Network List object by the specified Network List object id.  Before you can apply security policies, you must first define the networks that you want to protect from malicious attacks. The first step in configuring Infoblox Cloud is to set up DNS Firewall by defining your remote networks. You identify these external networks by their IP addresses. A network can contain a group of  or IPv6 addresses or blocks.  

### Example

```python
import os
from pprint import pprint

import fw

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.NetworkListsApi(api_client)
    id = 56 # int | The Network List object identifier.

    try:
        # Delete Network Lists.
        api_instance.delete_single_network_lists(id)
    except Exception as e:
        pprint("Exception when calling NetworkListsApi->delete_single_network_lists: %s\n" % e)
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

# **list_network_lists**
> NetworkListMultiResponse list_network_lists(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token)

List Network Lists.

Use this method to retrieve information on all Network List objects for the account.  Before you can apply security policies, you must first define the networks that you want to protect from malicious attacks. The first step in configuring Infoblox Cloud is to set up DNS Firewall by defining your remote networks. You identify these external networks by their IP addresses. A network can contain a group of IPv4 or IPv6 addresses or blocks.  

### Example

```python
import os
from pprint import pprint

import fw

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.NetworkListsApi(api_client)

    try:
        # List Network Lists.
        api_response = api_instance.list_network_lists()
        pprint("The response of NetworkListsApi->list_network_lists:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling NetworkListsApi->list_network_lists: %s\n" % e)
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

# **read_network_list**
> NetworkListReadResponse read_network_list(id, fields=fields, name=name)

Read Network List.

Use this method to retrieve information on the specified Network List object.  Before you can apply security policies, you must first define the networks that you want to protect from malicious attacks. The first step in configuring Infoblox Cloud is to set up DNS Firewall by defining your remote networks. You identify these external networks by their IP addresses. A network can contain a group of IPv4 or IPv6 addresses or blocks. 

### Example

```python
import os
from pprint import pprint

import fw

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.NetworkListsApi(api_client)
    id = 56 # int | The Network List object identifier.

    try:
        # Read Network List.
        api_response = api_instance.read_network_list(id)
        pprint("The response of NetworkListsApi->read_network_list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling NetworkListsApi->read_network_list: %s\n" % e)
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

# **update_network_list**
> NetworkListUpdateResponse update_network_list(id, body)

Update Network List.

Use this method to update a specified Network List object.  Before you can apply security policies, you must first define the networks that you want to protect from malicious attacks. The first step in configuring Infoblox Cloud is to set up DNS Firewall by defining your remote networks. You identify these external networks by their IP addresses. A network can contain a group of IPv4 or IPv6 addresses or blocks.  Required: - name - items 

### Example

```python
import os
from pprint import pprint

import fw

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fw.NetworkListsApi(api_client)
    id = 56 # int | The Network List object identifier.
    body = fw.NetworkList() # NetworkList | The Network List object.

    try:
        # Update Network List.
        api_response = api_instance.update_network_list(id, body)
        pprint("The response of NetworkListsApi->update_network_list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling NetworkListsApi->update_network_list: %s\n" % e)
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
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;name&#39; value cannot be equal to &#39;All Infoblox Endpoints (Default)&#39;, &#39;All Networks (Default)&#39;, &#39;All DNS Forwarder Proxies (Default)&#39; - &#39;description&#39; length cannot exceed 256 characters limit - &#39;items&#39; value must not be empty - &#39;items&#39; value must contain valid CIDRs from range [24, 32] - CIDRs in &#39;items&#39; cannot overlap with each other and with existing items for all accounts |  -  |
**404** |  - &#39;id&#39; value must contain existing network list identifier |  -  |
**409** |  - &#39;name&#39; value must be unique among network lists belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

