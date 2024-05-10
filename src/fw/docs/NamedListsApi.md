# fw.NamedListsApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateNamedList**](NamedListsApi.md#CreateNamedList) | **POST** /named_lists | Create Named List.
[**DeleteNamedLists**](NamedListsApi.md#DeleteNamedLists) | **DELETE** /named_lists | Delete Named Lists.
[**DeleteSingleNamedLists**](NamedListsApi.md#DeleteSingleNamedLists) | **DELETE** /named_lists/{id} | Delete Named Lists.
[**ListNamedLists**](NamedListsApi.md#ListNamedLists) | **GET** /named_lists | List Named Lists.
[**ListNamedListsCSV**](NamedListsApi.md#ListNamedListsCSV) | **GET** /named_lists_download | List Named Lists in CSV format.
[**MultiListUpdate**](NamedListsApi.md#MultiListUpdate) | **PATCH** /named_lists | Patch Multiple Named Lists.
[**ReadNamedList**](NamedListsApi.md#ReadNamedList) | **GET** /named_lists/{id} | Read Named List.
[**UpdateNamedList**](NamedListsApi.md#UpdateNamedList) | **PUT** /named_lists/{id} | Update Named List.
[**UpdateNamedListPartial**](NamedListsApi.md#UpdateNamedListPartial) | **PATCH** /named_lists/{id} | Patch TI List.


# **CreateNamedList**
> NamedListCreateResponse CreateNamedList(body)

Create Named List.

Use this method to create a Named List object.  The Named List object represents several types of lists allowed for BloxOne Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed. Note that lists representing predefined TI feeds cannot be created, updated and deleted. Also use of the field 'items' is discouraged and instead use of new field 'item_described' is suggested as it is possible to add the description/comments to each item in the custom list using this field. In any case, note that use of both the fields 'items' and 'items_described' is not supported and when one of these field is used they must have some value i.e, it cannot be empty.  Required: - name - type - items or items_described 

### Example


```python
import fw
from fw.models.named_list import NamedList
from fw.models.named_list_create_response import NamedListCreateResponse
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
    api_instance = fw.NamedListsApi(api_client)
    body = fw.NamedList() # NamedList | The Named List object.

    try:
        # Create Named List.
        api_response = api_instance.CreateNamedList(body)
        print("The response of NamedListsApi->CreateNamedList:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamedListsApi->CreateNamedList: %s\n" % e)
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

# **DeleteNamedLists**
> DeleteNamedLists(body)

Delete Named Lists.

Use this method to delete Named List objects. Deletion of multiple lists is an all-or-nothing operation (if any of the specified lists can not be deleted then none of the specified lists will be deleted).  The Named List object represents several types of lists allowed for BloxOne Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed. Note that lists representing predefined TI feeds cannot be created, updated and deleted.  Required: - ids 

### Example


```python
import fw
from fw.models.named_lists_delete_request import NamedListsDeleteRequest
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
    api_instance = fw.NamedListsApi(api_client)
    body = fw.NamedListsDeleteRequest() # NamedListsDeleteRequest | 

    try:
        # Delete Named Lists.
        api_instance.DeleteNamedLists(body)
    except Exception as e:
        print("Exception when calling NamedListsApi->DeleteNamedLists: %s\n" % e)
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

# **DeleteSingleNamedLists**
> DeleteSingleNamedLists(id)

Delete Named Lists.

Use this method to delete Named List object by given Named List object identifier.  The Named List object represents several types of lists allowed for BloxOne Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed. Note that lists representing predefined TI feeds cannot be created, updated and deleted. 

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
    api_instance = fw.NamedListsApi(api_client)
    id = 56 # int | The Named List object identifiers.

    try:
        # Delete Named Lists.
        api_instance.DeleteSingleNamedLists(id)
    except Exception as e:
        print("Exception when calling NamedListsApi->DeleteSingleNamedLists: %s\n" % e)
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

# **ListNamedLists**
> NamedListReadMultiResponse ListNamedLists(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)

List Named Lists.

Use this method to retrieve information on all Named List objects for the account. Note that list items are not returned for this operation.  The Named List object represents several types of lists allowed for BloxOne Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed. Note that lists representing predefined TI feeds cannot be created, updated and deleted.   

### Example


```python
import fw
from fw.models.named_list_read_multi_response import NamedListReadMultiResponse
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
    api_instance = fw.NamedListsApi(api_client)
    filter = 'filter_example' # str | A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name               | type   | Supported Ops    | | ------------------ | ------ | ---------------- | | type               | string | ==, !=           | | items              | string | ~, !~            | | items_described    | string | ==               |  Grouping operators (and, or, not, ()) are not supported between different fields.  (optional)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
    limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
    page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
    tfilter = 'tfilter_example' # str | Filtering by tags. (optional)
    torder_by = 'torder_by_example' # str | Sorting by tags. (optional)

    try:
        # List Named Lists.
        api_response = api_instance.ListNamedLists(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)
        print("The response of NamedListsApi->ListNamedLists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamedListsApi->ListNamedLists: %s\n" % e)
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

# **ListNamedListsCSV**
> NamedListCSVListResponse ListNamedListsCSV(filter=filter, order_by=order_by, tfilter=tfilter, torder_by=torder_by)

List Named Lists in CSV format.

Use this method to download the selected list of named lists in CSV (comma-separate values) format.  

### Example


```python
import fw
from fw.models.named_list_csv_list_response import NamedListCSVListResponse
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
    api_instance = fw.NamedListsApi(api_client)
    filter = 'filter_example' # str | A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name               | type   | Supported Ops    | | ------------------ | ------ | ---------------- | | type               | string | ==, !=           | | items              | string | ~, !~            | | items_described    | string | ==               |  Grouping operators (and, or, not, ()) are not supported between different fields.  (optional)
    order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
    tfilter = 'tfilter_example' # str | Filtering by tags. (optional)
    torder_by = 'torder_by_example' # str | Sorting by tags. (optional)

    try:
        # List Named Lists in CSV format.
        api_response = api_instance.ListNamedListsCSV(filter=filter, order_by=order_by, tfilter=tfilter, torder_by=torder_by)
        print("The response of NamedListsApi->ListNamedListsCSV:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamedListsApi->ListNamedListsCSV: %s\n" % e)
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

# **MultiListUpdate**
> object MultiListUpdate(body)

Patch Multiple Named Lists.

Multiple Named Lists in a single operation. Use this method to insert items for multiple Named List objects. Note that duplicated items correspondig to named list are silently skipped and only new items are appended to the named list. Note that DNSM, TI, Fast Flux and DGA lists cannot be updated. Only named lists of Custom List type can be updated by this operation. If one or more of the list ids is invalid, or the list is of invalid type then the entire operation will be failed. The Custom List Items represent the list of the FQDN or IPv4 addresses to define whitelists and blacklists for additional protection.

### Example


```python
import fw
from fw.models.multi_list_update import MultiListUpdate
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
    api_instance = fw.NamedListsApi(api_client)
    body = fw.MultiListUpdate() # MultiListUpdate | 

    try:
        # Patch Multiple Named Lists.
        api_response = api_instance.MultiListUpdate(body)
        print("The response of NamedListsApi->MultiListUpdate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamedListsApi->MultiListUpdate: %s\n" % e)
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

# **ReadNamedList**
> NamedListReadResponse ReadNamedList(id, fields=fields, offset=offset, limit=limit, page_token=page_token, name=name, type=type)

Read Named List.

Use this method to retrieve information on the specified Named List object. Note that returned data includes list items.  The Named List object represents several types of lists allowed for BloxOne Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed. Note that lists representing predefined TI feeds cannot be created, updated and deleted. 

### Example


```python
import fw
from fw.models.named_list_read_response import NamedListReadResponse
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
    api_instance = fw.NamedListsApi(api_client)
    id = 56 # int | The Named List identifier.
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
    limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
    page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
    name = 'name_example' # str | The name of the named list. Can be used in pair with 'type' (both fields are mandatory) to request the object by their name. This aproach available only if the field 'id' is empty (==0). (optional)
    type = 'type_example' # str | The type of the named list. See 'NamedList' for more details. (optional)

    try:
        # Read Named List.
        api_response = api_instance.ReadNamedList(id, fields=fields, offset=offset, limit=limit, page_token=page_token, name=name, type=type)
        print("The response of NamedListsApi->ReadNamedList:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamedListsApi->ReadNamedList: %s\n" % e)
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

# **UpdateNamedList**
> NamedListUpdateResponse UpdateNamedList(id, body)

Update Named List.

Use this method to update the specified Named List object. Note that list type cannot be updated.  The Named List object represents several types of lists allowed for BloxOne Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed. Note that lists representing predefined TI feeds cannot be created, updated and deleted. Also use of the field 'items' is discouraged and instead use of new field 'item_described' is suggested as it is possible to add the description/comments to each item in the custom list using this field. In any case, note that use of both the fields 'items' and 'items_described' is not supported and when one of these field is used they must have some value i.e, it cannot be empty.  Required: - name - items or items_described 

### Example


```python
import fw
from fw.models.named_list import NamedList
from fw.models.named_list_update_response import NamedListUpdateResponse
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
    api_instance = fw.NamedListsApi(api_client)
    id = 56 # int | The Named List object identifier.
    body = fw.NamedList() # NamedList | The Named List object.

    try:
        # Update Named List.
        api_response = api_instance.UpdateNamedList(id, body)
        print("The response of NamedListsApi->UpdateNamedList:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamedListsApi->UpdateNamedList: %s\n" % e)
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

# **UpdateNamedListPartial**
> NamedListUpdateResponse UpdateNamedListPartial(id, body)

Patch TI List.

Use this method to update the Severity for a specified named list, which must be of TI list type.  The severity levels (threat_level and confidence_level) can only be patched for a given id of a TI List. This patch request only accepts threat_level and confidence level as the attributes. At least one of these two attributes must be present in the request. If only one of the two attributes is present, only that attribute is set to the specified value for the specified list and other attribute will be at the present value. This operation is currently applicable only for the TI Lists.  Required: - id - threat_level or confidence_level 

### Example


```python
import fw
from fw.models.list_severity_levels import ListSeverityLevels
from fw.models.named_list_update_response import NamedListUpdateResponse
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
    api_instance = fw.NamedListsApi(api_client)
    id = 56 # int | The Named List object identifier.
    body = fw.ListSeverityLevels() # ListSeverityLevels | The Named List object.

    try:
        # Patch TI List.
        api_response = api_instance.UpdateNamedListPartial(id, body)
        print("The response of NamedListsApi->UpdateNamedListPartial:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamedListsApi->UpdateNamedListPartial: %s\n" % e)
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

