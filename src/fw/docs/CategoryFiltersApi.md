# fw.CategoryFiltersApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_category_filter**](CategoryFiltersApi.md#create_category_filter) | **POST** /category_filters | Create Category Filter.
[**delete_category_filters**](CategoryFiltersApi.md#delete_category_filters) | **DELETE** /category_filters | Delete Category Filters By ID.
[**delete_single_category_filters**](CategoryFiltersApi.md#delete_single_category_filters) | **DELETE** /category_filters/{id} | Delete Category Filters.
[**list_category_filters**](CategoryFiltersApi.md#list_category_filters) | **GET** /category_filters | List Category Filters.
[**read_category_filter**](CategoryFiltersApi.md#read_category_filter) | **GET** /category_filters/{id} | Read Category Filter.
[**update_category_filter**](CategoryFiltersApi.md#update_category_filter) | **PUT** /category_filters/{id} | Update Category Filter.


# **create_category_filter**
> CategoryFilterCreateResponse create_category_filter(body)

Create Category Filter.

Use this method to create a Category Filter object.  Category filters are content categorization rules that Infoblox Cloud uses to detect and filter specific internet content. Based on your configuration, specific actions such as Allow or Block, will be taken on the detected content. Infoblox Cloud provides the following content categories from which you can build your category filters: Drugs, Risk/Fraud/Crime, Entertainment/Culture, Purchasing, Information/Communication, Business/Services, Information Technology, Lifestyle, Society/Education/Religion, Mature/Violent, Games/Gambling, Pornography/Nudity and Uncategorized. Each of these categories contains sub-categories that further define the respective content. When you configure your category filter, you can add as many sub-categories as you need. You then add the category filter to your security policy and assign the Block action for the filter.  Required: - name - categories 

### Example

```python
import os
from pprint import pprint

import fw

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = fw.CategoryFiltersApi(api_client)
    body = fw.CategoryFilter() # CategoryFilter | The Category Filter object.

    try:
        # Create Category Filter.
        api_response = api_instance.create_category_filter(body)
        pprint("The response of CategoryFiltersApi->create_category_filter:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling CategoryFiltersApi->create_category_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CategoryFilter**](CategoryFilter.md)| The Category Filter object. | 

### Return type

[**CategoryFilterCreateResponse**](CategoryFilterCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |
**400** |  - &#39;name&#39; value must not be empty - &#39;name&#39; length cannot exceed 256 characters limit - &#39;description&#39; length cannot exceed 256 characters limit - &#39;categories&#39; value must not be empty - &#39;categories&#39; value must contain existing content categories |  -  |
**409** |  - &#39;name&#39; value must be unique among category filters belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category_filters**
> delete_category_filters(body)

Delete Category Filters By ID.

Use this method to delete Category Filter object.  Category filters are content categorization rules that Infoblox Cloud uses to detect and filter specific internet content. Based on your configuration, specific actions such as Allow or Block, will be taken on the detected content. Infoblox Cloud provides the following content categories from which you can build your category filters: Drugs, Risk/Fraud/Crime, Entertainment/Culture, Purchasing, Information/Communication, Business/Services, Information Technology, Lifestyle, Society/Education/Religion, Mature/Violent, Games/Gambling, Pornography/Nudity and Uncategorized. Each of these categories contains sub-categories that further define the respective content. When you configure your category filter, you can add as many sub-categories as you need. You then add the category filter to your security policy and assign the Block action for the filter.  Required: - ids  

### Example

```python
import os
from pprint import pprint

import fw

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = fw.CategoryFiltersApi(api_client)
    body = fw.CategoryFiltersDeleteRequest() # CategoryFiltersDeleteRequest | 

    try:
        # Delete Category Filters By ID.
        api_instance.delete_category_filters(body)
    except Exception as e:
        pprint("Exception when calling CategoryFiltersApi->delete_category_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CategoryFiltersDeleteRequest**](CategoryFiltersDeleteRequest.md)|  | 

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
**400** |  - &#39;ids&#39; value must be non-empty - &#39;ids&#39; value must contain unique elements - &#39;ids&#39; value must contain values that are greater than or equal to zero - category filters assigned to a security policy cannot be deleted - category filters assigned to a bypass code cannot be deleted - &#39;ids&#39; value must contain existing category filter identifiers |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_single_category_filters**
> delete_single_category_filters(id)

Delete Category Filters.

Use this method to delete Category Filter objects.  Category filters are content categorization rules that Infoblox Cloud uses to detect and filter specific internet content. Based on your configuration, specific actions such as Allow or Block, will be taken on the detected content. Infoblox Cloud provides the following content categories from which you can build your category filters: Drugs, Risk/Fraud/Crime, Entertainment/Culture, Purchasing, Information/Communication, Business/Services, Information Technology, Lifestyle, Society/Education/Religion, Mature/Violent, Games/Gambling, Pornography/Nudity and Uncategorized. Each of these categories contains sub-categories that further define the respective content. When you configure your category filter, you can add as many sub-categories as you need. You then add the category filter to your security policy and assign the Block action for the filter. 

### Example

```python
import os
from pprint import pprint

import fw

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = fw.CategoryFiltersApi(api_client)
    id = 56 # int | The Category Filter object identifier.

    try:
        # Delete Category Filters.
        api_instance.delete_single_category_filters(id)
    except Exception as e:
        pprint("Exception when calling CategoryFiltersApi->delete_single_category_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Category Filter object identifier. | 

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
**400** |  - &#39;id&#39; value must contain values that are greater than or equal to zero - &#39;ids&#39; value must contain existing category filter identifiers - category filter assigned to a security policy cannot be deleted - category filter assigned to a bypass code cannot be deleted |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_category_filters**
> CategoryFilterMultiResponse list_category_filters(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)

List Category Filters.

Use this method to retrieve information on all Category Filter objects for the account.  Category filters are content categorization rules that Infoblox Cloud uses to detect and filter specific internet content. Based on your configuration, specific actions such as Allow or Block, will be taken on the detected content. Infoblox Cloud provides the following content categories from which you can build your category filters: Drugs, Risk/Fraud/Crime, Entertainment/Culture, Purchasing, Information/Communication, Business/Services, Information Technology, Lifestyle, Society/Education/Religion, Mature/Violent, Games/Gambling, Pornography/Nudity and Uncategorized. Each of these categories contains sub-categories that further define the respective content. When you configure your category filter, you can add as many sub-categories as you need. You then add the category filter to your security policy and assign the Block action for the filter.  

### Example

```python
import os
from pprint import pprint

import fw

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = fw.CategoryFiltersApi(api_client)

    try:
        # List Category Filters.
        api_response = api_instance.list_category_filters()
        pprint("The response of CategoryFiltersApi->list_category_filters:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling CategoryFiltersApi->list_category_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;.  You can filter by following fields:  | Name               | type   | Supported Op                | | ------------------ | ------ | --------------------------- | | name               | string | !&#x3D;, &#x3D;&#x3D;, ~, !~, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D; |  In addition, grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Groupping Operators  |  Example: &#x60;&#x60;&#x60; ?_filter&#x3D;\&quot;((name&#x3D;&#x3D;&#39;cat-filter&#39;)or(name~&#39;key&#39;))and(name!&#x3D;&#39;something&#39;)\&quot; &#x60;&#x60;&#x60;  | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **tfilter** | **str**| Filtering by tags. | [optional] 
 **torder_by** | **str**| Sorting by tags. | [optional] 

### Return type

[**CategoryFilterMultiResponse**](CategoryFilterMultiResponse.md)

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

# **read_category_filter**
> CategoryFilterReadResponse read_category_filter(id, fields=fields, name=name)

Read Category Filter.

Use this method to retrieve information on the specified Category Filter object.  Category filters are content categorization rules that Infoblox Cloud uses to detect and filter specific internet content. Based on your configuration, specific actions such as Allow or Block, will be taken on the detected content. Infoblox Cloud provides the following content categories from which you can build your category filters: Drugs, Risk/Fraud/Crime, Entertainment/Culture, Purchasing, Information/Communication, Business/Services, Information Technology, Lifestyle, Society/Education/Religion, Mature/Violent, Games/Gambling, Pornography/Nudity and Uncategorized. Each of these categories contains sub-categories that further define the respective content. When you configure your category filter, you can add as many sub-categories as you need. You then add the category filter to your security policy and assign the Block action for the filter. 

### Example

```python
import os
from pprint import pprint

import fw

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = fw.CategoryFiltersApi(api_client)
    id = 56 # int | The Category Filter object identifier.

    try:
        # Read Category Filter.
        api_response = api_instance.read_category_filter(id)
        pprint("The response of CategoryFiltersApi->read_category_filter:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling CategoryFiltersApi->read_category_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Category Filter object identifier. | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**CategoryFilterReadResponse**](CategoryFilterReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |
**404** |  - &#39;id&#39; value must contain existing category filter identifier |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category_filter**
> CategoryFilterUpdateResponse update_category_filter(id, body)

Update Category Filter.

Use this method to update the specified Category Filter object.  Category filters are content categorization rules that Infoblox Cloud uses to detect and filter specific internet content. Based on your configuration, specific actions such as Allow or Block, will be taken on the detected content. Infoblox Cloud provides the following content categories from which you can build your category filters: Drugs, Risk/Fraud/Crime, Entertainment/Culture, Purchasing, Information/Communication, Business/Services, Information Technology, Lifestyle, Society/Education/Religion, Mature/Violent, Games/Gambling, Pornography/Nudity and Uncategorized. Each of these categories contains sub-categories that further define the respective content. When you configure your category filter, you can add as many sub-categories as you need. You then add the category filter to your security policy and assign the Block action for the filter.  Required: - name - categories 

### Example

```python
import os
from pprint import pprint

import fw

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = fw.CategoryFiltersApi(api_client)
    id = 56 # int | The Category Filter object identifier.
    body = fw.CategoryFilter() # CategoryFilter | The Category Filter object.

    try:
        # Update Category Filter.
        api_response = api_instance.update_category_filter(id, body)
        pprint("The response of CategoryFiltersApi->update_category_filter:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling CategoryFiltersApi->update_category_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Category Filter object identifier. | 
 **body** | [**CategoryFilter**](CategoryFilter.md)| The Category Filter object. | 

### Return type

[**CategoryFilterUpdateResponse**](CategoryFilterUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PUT operation response |  -  |
**400** |  - &#39;name&#39; value must not be empty - &#39;name&#39; length cannot exceed 256 characters limit - &#39;description&#39; length cannot exceed 256 characters limit - &#39;categories&#39; value must not be empty - &#39;categories&#39; value must contain existing content categories |  -  |
**404** |  - &#39;id&#39; value must contain existing category filter identifier |  -  |
**409** |  - &#39;name&#39; value must be unique among category filters belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

