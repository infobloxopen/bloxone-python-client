# fw.PopRegionsApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ListPoPRegions**](PopRegionsApi.md#ListPoPRegions) | **GET** /pop_regions | List PoP Regions.
[**ReadPoPRegion**](PopRegionsApi.md#ReadPoPRegion) | **GET** /pop_regions/{id} | Read PoP Region.


# **ListPoPRegions**
> ListPoPRegionsResponse ListPoPRegions(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)

List PoP Regions.

Use this method to retrieve information on all Point of Presence (PoP) regions availablein the database.  

### Example


```python
import fw
from fw.models.list_po_p_regions_response import ListPoPRegionsResponse
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
    api_instance = fw.PopRegionsApi(api_client)
    filter = 'filter_example' # str | A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name               | type   | Supported Ops    | | ------------------ | ------ | ---------------- | | region             | string | ==, !=           | | location           | string | ~, !~            |  Grouping operators (and, or, not, ()) are not supported between different fields.  (optional)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
    limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
    page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
    tfilter = 'tfilter_example' # str | Filtering by tags. (optional)
    torder_by = 'torder_by_example' # str | Sorting by tags. (optional)

    try:
        # List PoP Regions.
        api_response = api_instance.ListPoPRegions(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)
        print("The response of PopRegionsApi->ListPoPRegions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PopRegionsApi->ListPoPRegions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;.  You can filter by following fields:  | Name               | type   | Supported Ops    | | ------------------ | ------ | ---------------- | | region             | string | &#x3D;&#x3D;, !&#x3D;           | | location           | string | ~, !~            |  Grouping operators (and, or, not, ()) are not supported between different fields.  | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **tfilter** | **str**| Filtering by tags. | [optional] 
 **torder_by** | **str**| Sorting by tags. | [optional] 

### Return type

[**ListPoPRegionsResponse**](ListPoPRegionsResponse.md)

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

# **ReadPoPRegion**
> ReadPoPRegionResponse ReadPoPRegion(id)

Read PoP Region.

Use this method to retrieve information on the specified PoP region object. 

### Example


```python
import fw
from fw.models.read_po_p_region_response import ReadPoPRegionResponse
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
    api_instance = fw.PopRegionsApi(api_client)
    id = 56 # int | The PoP region object identifier

    try:
        # Read PoP Region.
        api_response = api_instance.ReadPoPRegion(id)
        print("The response of PopRegionsApi->ReadPoPRegion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PopRegionsApi->ReadPoPRegion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The PoP region object identifier | 

### Return type

[**ReadPoPRegionResponse**](ReadPoPRegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |
**404** |  - &#39;id&#39; value must contain existing PoP region&#39;s id  |  -  |
**500** |  - Internal server error occurred  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

