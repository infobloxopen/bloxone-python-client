# fw.NamedListsApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_named_list**](NamedListsApi.md#create_named_list) | **POST** /named_lists | Create Named List.
[**delete_named_lists**](NamedListsApi.md#delete_named_lists) | **DELETE** /named_lists | Delete Named Lists.
[**delete_single_named_lists**](NamedListsApi.md#delete_single_named_lists) | **DELETE** /named_lists/{id} | Delete Named Lists.
[**list_named_lists**](NamedListsApi.md#list_named_lists) | **GET** /named_lists | List Named Lists.
[**list_named_lists_csv**](NamedListsApi.md#list_named_lists_csv) | **GET** /named_lists_download | List Named Lists in CSV format.
[**multi_list_update**](NamedListsApi.md#multi_list_update) | **PATCH** /named_lists | Patch Multiple Named Lists.
[**read_named_list**](NamedListsApi.md#read_named_list) | **GET** /named_lists/{id} | Read Named List.
[**update_named_list**](NamedListsApi.md#update_named_list) | **PUT** /named_lists/{id} | Update Named List.
[**update_named_list_partial**](NamedListsApi.md#update_named_list_partial) | **PATCH** /named_lists/{id} | Patch TI List.


# **create_named_list**
> NamedListCreateResponse create_named_list(body)

Create Named List.

Use this method to create a Named List object.  The Named List object represents several types of lists allowed for Infoblox Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed. Note that lists representing predefined TI feeds cannot be created, updated and deleted. Also use of the field 'items' is discouraged and instead use of new field 'item_described' is suggested as it is possible to add the description/comments to each item in the custom list using this field. In any case, note that use of both the fields 'items' and 'items_described' is not supported and when one of these field is used they must have some value i.e, it cannot be empty.  Required: - name - type - items or items_described 

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
    api_instance = fw.NamedListsApi(api_client)
    body = fw.NamedList() # NamedList | The Named List object.

    try:
        # Create Named List.
        api_response = api_instance.create_named_list(body)
        pprint("The response of NamedListsApi->create_named_list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling NamedListsApi->create_named_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NamedList**](NamedList.md)| The Named List object. | 

### Return type

[**NamedListCreateResponse**](NamedListCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;description&#39; length cannot exceed 256 characters limit - &#39;items&#39; value must contain valid IPv4 or IPv6 addresses or domain names - named list of type \&quot;dnsm\&quot;, \&quot;threat_insight\&quot;, \&quot;fast_flux\&quot;, \&quot;dga\&quot;, \&quot;threat_insight_nde\&quot;, \&quot;default_allow\&quot;, \&quot;default_block\&quot;, \&quot;threat_insight_nde\&quot; cannot be created - Either &#39;items&#39; or &#39;items_described&#39; field is required - &#39;item&#39; cannot be empty in field items_described |  -  |
**409** |  - &#39;name&#39; value must be unique among named lists belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_named_lists**
> delete_named_lists(body)

Delete Named Lists.

Use this method to delete Named List objects. Deletion of multiple lists is an all-or-nothing operation (if any of the specified lists can not be deleted then none of the specified lists will be deleted).  The Named List object represents several types of lists allowed for Infoblox Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed. Note that lists representing predefined TI feeds cannot be created, updated and deleted.  Required: - ids 

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
    api_instance = fw.NamedListsApi(api_client)
    body = fw.NamedListsDeleteRequest() # NamedListsDeleteRequest | 

    try:
        # Delete Named Lists.
        api_instance.delete_named_lists(body)
    except Exception as e:
        pprint("Exception when calling NamedListsApi->delete_named_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NamedListsDeleteRequest**](NamedListsDeleteRequest.md)|  | 

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
**400** |  - &#39;ids&#39; value must be non-empty - &#39;ids&#39; value must contain unique elements - &#39;ids&#39; value must contain values that are greater than or equal to zero - named lists assigned to a security policy cannot be deleted - named lists of type &#39;dnsm&#39;, &#39;threat_insight&#39;, &#39;fast_flux&#39;, &#39;dga&#39;, &#39;threat_insight_nde&#39;, &#39;default_allow&#39; and &#39;default_block&#39; cannot be removed - named lists assigned to a bypass code cannot be deleted |  -  |
**404** |  - &#39;ids&#39; value must contain existing named list identifiers |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_single_named_lists**
> delete_single_named_lists(id)

Delete Named Lists.

Use this method to delete Named List object by given Named List object identifier.  The Named List object represents several types of lists allowed for Infoblox Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed. Note that lists representing predefined TI feeds cannot be created, updated and deleted. 

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
    api_instance = fw.NamedListsApi(api_client)
    id = 56 # int | The Named List object identifiers.

    try:
        # Delete Named Lists.
        api_instance.delete_single_named_lists(id)
    except Exception as e:
        pprint("Exception when calling NamedListsApi->delete_single_named_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Named List object identifiers. | 

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
**400** |  - &#39;id&#39; value must contain values that are greater than or equal to zero - named lists assigned to a security policy cannot be deleted - named lists assigned to a bypass code cannot be deleted - named lists of type &#39;dnsm&#39;, &#39;threat_insight&#39;, &#39;fast_flux&#39;, &#39;dga&#39;, &#39;threat_insight_nde&#39;, &#39;default_allow&#39;, and &#39;default_block&#39; cannot be removed |  -  |
**404** |  - &#39;id&#39; value must contain existing named list identifiers |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_named_lists**
> NamedListReadMultiResponse list_named_lists(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)

List Named Lists.

Use this method to retrieve information on all Named List objects for the account. Note that list items are not returned for this operation.  The Named List object represents several types of lists allowed for Infoblox Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed. Note that lists representing predefined TI feeds cannot be created, updated and deleted.   

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
    api_instance = fw.NamedListsApi(api_client)

    try:
        # List Named Lists.
        api_response = api_instance.list_named_lists()
        pprint("The response of NamedListsApi->list_named_lists:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling NamedListsApi->list_named_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;.  You can filter by following fields:  | Name               | type   | Supported Ops    | | ------------------ | ------ | ---------------- | | type               | string | &#x3D;&#x3D;, !&#x3D;           | | items              | string | ~, !~            | | items_described    | string | &#x3D;&#x3D;               |  Grouping operators (and, or, not, ()) are not supported between different fields.  | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **tfilter** | **str**| Filtering by tags. | [optional] 
 **torder_by** | **str**| Sorting by tags. | [optional] 

### Return type

[**NamedListReadMultiResponse**](NamedListReadMultiResponse.md)

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

# **list_named_lists_csv**
> NamedListCSVListResponse list_named_lists_csv(filter=filter, order_by=order_by, tfilter=tfilter, torder_by=torder_by)

List Named Lists in CSV format.

Use this method to download the selected list of named lists in CSV (comma-separate values) format.  

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
    api_instance = fw.NamedListsApi(api_client)

    try:
        # List Named Lists in CSV format.
        api_response = api_instance.list_named_lists_csv()
        pprint("The response of NamedListsApi->list_named_lists_csv:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling NamedListsApi->list_named_lists_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;.  You can filter by following fields:  | Name               | type   | Supported Ops    | | ------------------ | ------ | ---------------- | | type               | string | &#x3D;&#x3D;, !&#x3D;           | | items              | string | ~, !~            | | items_described    | string | &#x3D;&#x3D;               |  Grouping operators (and, or, not, ()) are not supported between different fields.  | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **tfilter** | **str**| Filtering by tags. | [optional] 
 **torder_by** | **str**| Sorting by tags. | [optional] 

### Return type

[**NamedListCSVListResponse**](NamedListCSVListResponse.md)

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

# **multi_list_update**
> object multi_list_update(body)

Patch Multiple Named Lists.

Multiple Named Lists in a single operation. Use this method to insert items for multiple Named List objects. Note that duplicated items correspondig to named list are silently skipped and only new items are appended to the named list. Note that DNSM, TI, Fast Flux and DGA lists cannot be updated. Only named lists of Custom List type can be updated by this operation. If one or more of the list ids is invalid, or the list is of invalid type then the entire operation will be failed. The Custom List Items represent the list of the FQDN or IPv4 addresses to define whitelists and blacklists for additional protection.

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
    api_instance = fw.NamedListsApi(api_client)
    body = fw.MultiListUpdate() # MultiListUpdate | 

    try:
        # Patch Multiple Named Lists.
        api_response = api_instance.multi_list_update(body)
        pprint("The response of NamedListsApi->multi_list_update:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling NamedListsApi->multi_list_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MultiListUpdate**](MultiListUpdate.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PATCH operation response |  -  |
**400** |  - &#39;ids&#39; values must be greater than or equal to zero - &#39;inserted_items_described&#39; value must contain either valid domain names or IPv4 or network addresses. |  -  |
**404** |  - &#39;ids&#39; values must contain existing named list identifier |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_named_list**
> NamedListReadResponse read_named_list(id, fields=fields, offset=offset, limit=limit, page_token=page_token, name=name, type=type)

Read Named List.

Use this method to retrieve information on the specified Named List object. Note that returned data includes list items.  The Named List object represents several types of lists allowed for Infoblox Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed. Note that lists representing predefined TI feeds cannot be created, updated and deleted. 

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
    api_instance = fw.NamedListsApi(api_client)
    id = 56 # int | The Named List identifier.

    try:
        # Read Named List.
        api_response = api_instance.read_named_list(id)
        pprint("The response of NamedListsApi->read_named_list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling NamedListsApi->read_named_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Named List identifier. | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **name** | **str**| The name of the named list. Can be used in pair with &#39;type&#39; (both fields are mandatory) to request the object by their name. This aproach available only if the field &#39;id&#39; is empty (&#x3D;&#x3D;0). | [optional] 
 **type** | **str**| The type of the named list. See &#39;NamedList&#39; for more details. | [optional] 

### Return type

[**NamedListReadResponse**](NamedListReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |
**404** |  - &#39;id&#39; value must contain existing named list identifier |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_named_list**
> NamedListUpdateResponse update_named_list(id, body)

Update Named List.

Use this method to update the specified Named List object. Note that list type cannot be updated.  The Named List object represents several types of lists allowed for Infoblox Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed. Note that lists representing predefined TI feeds cannot be created, updated and deleted. Also use of the field 'items' is discouraged and instead use of new field 'item_described' is suggested as it is possible to add the description/comments to each item in the custom list using this field. In any case, note that use of both the fields 'items' and 'items_described' is not supported and when one of these field is used they must have some value i.e, it cannot be empty.  Required: - name - items or items_described 

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
    api_instance = fw.NamedListsApi(api_client)
    id = 56 # int | The Named List object identifier.
    body = fw.NamedList() # NamedList | The Named List object.

    try:
        # Update Named List.
        api_response = api_instance.update_named_list(id, body)
        pprint("The response of NamedListsApi->update_named_list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling NamedListsApi->update_named_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Named List object identifier. | 
 **body** | [**NamedList**](NamedList.md)| The Named List object. | 

### Return type

[**NamedListUpdateResponse**](NamedListUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PUT operation response |  -  |
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;description&#39; length cannot exceed 256 characters limit - &#39;items&#39; value must contain valid IPv4 addresses or domain names - named list of type \&quot;dnsm\&quot;, \&quot;threat_insight\&quot;, \&quot;fast_flux\&quot;, \&quot;dga\&quot; and \&quot;threat_insight_nde\&quot; cannot be created - list type cannot be updated - Either &#39;items&#39; or &#39;items_described&#39; field is required - &#39;item&#39; cannot be empty in field items_described |  -  |
**404** |  - &#39;id&#39; value must contain existing named list identifier |  -  |
**409** |  - &#39;name&#39; value must be unique among named lists belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_named_list_partial**
> NamedListUpdateResponse update_named_list_partial(id, body)

Patch TI List.

Use this method to update the Severity for a specified named list, which must be of TI list type.  The severity levels (threat_level and confidence_level) can only be patched for a given id of a TI List. This patch request only accepts threat_level and confidence level as the attributes. At least one of these two attributes must be present in the request. If only one of the two attributes is present, only that attribute is set to the specified value for the specified list and other attribute will be at the present value. This operation is currently applicable only for the TI Lists.  Required: - id - threat_level or confidence_level 

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
    api_instance = fw.NamedListsApi(api_client)
    id = 56 # int | The Named List object identifier.
    body = fw.ListSeverityLevels() # ListSeverityLevels | The Named List object.

    try:
        # Patch TI List.
        api_response = api_instance.update_named_list_partial(id, body)
        pprint("The response of NamedListsApi->update_named_list_partial:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling NamedListsApi->update_named_list_partial: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Named List object identifier. | 
 **body** | [**ListSeverityLevels**](ListSeverityLevels.md)| The Named List object. | 

### Return type

[**NamedListUpdateResponse**](NamedListUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PATCH operation response |  -  |
**400** |  - Either &#39;threat_level&#39; or &#39;confidence_level&#39; field is required - Operation not supported for type &#39;custom_list&#39;  |  -  |
**404** |  - &#39;id&#39; value must contain existing named list identifier |  -  |
**405** |  - Only PATCH operation supported for the existing TI Lists |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

