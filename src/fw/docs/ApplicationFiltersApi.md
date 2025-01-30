# fw.ApplicationFiltersApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application_filter**](ApplicationFiltersApi.md#create_application_filter) | **POST** /application_filters | Create Application Filter.
[**delete_application_filters**](ApplicationFiltersApi.md#delete_application_filters) | **DELETE** /application_filters | Delete Application Filters.
[**delete_single_application_filters**](ApplicationFiltersApi.md#delete_single_application_filters) | **DELETE** /application_filters/{id} | Delete Application Filter Object by ID.
[**list_application_filters**](ApplicationFiltersApi.md#list_application_filters) | **GET** /application_filters | List Application Filters.
[**read_application_filter**](ApplicationFiltersApi.md#read_application_filter) | **GET** /application_filters/{id} | Read Application Filter.
[**update_application_filter**](ApplicationFiltersApi.md#update_application_filter) | **PUT** /application_filters/{id} | Update Application Filter.


# **create_application_filter**
> ApplicationFilterCreateResponse create_application_filter(body)

Create Application Filter.

Use this method to create a Application Filter object.  Required: - name - criteria 

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
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = fw.ApplicationFiltersApi(api_client)
    body = fw.ApplicationFilter() # ApplicationFilter | The Application Filter object.

    try:
        # Create Application Filter.
        api_response = api_instance.create_application_filter(body)
        pprint("The response of ApplicationFiltersApi->create_application_filter:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling ApplicationFiltersApi->create_application_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationFilter**](ApplicationFilter.md)| The Application Filter object. | 

### Return type

[**ApplicationFilterCreateResponse**](ApplicationFilterCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_filters**
> delete_application_filters(body)

Delete Application Filters.

Use this method to delete Application Filter objects. Deletion of multiple lists is an all-or-nothing operation (if any of the specified lists can not be deleted then none of the specified lists will be deleted).  Required: - ids  

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
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = fw.ApplicationFiltersApi(api_client)
    body = fw.ApplicationFiltersDeleteRequest() # ApplicationFiltersDeleteRequest | 

    try:
        # Delete Application Filters.
        api_instance.delete_application_filters(body)
    except Exception as e:
        pprint("Exception when calling ApplicationFiltersApi->delete_application_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationFiltersDeleteRequest**](ApplicationFiltersDeleteRequest.md)|  | 

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
**400** |  - &#39;ids&#39; value must contain existing application filter identifiers - application filters assigned to a security policy cannot be deleted - application filters assigned to a bypass code cannot be deleted |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_single_application_filters**
> delete_single_application_filters(id)

Delete Application Filter Object by ID.

Use this method to delete single Application filter object by id. 

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
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = fw.ApplicationFiltersApi(api_client)
    id = 56 # int | The Application Filter object identifier.

    try:
        # Delete Application Filter Object by ID.
        api_instance.delete_single_application_filters(id)
    except Exception as e:
        pprint("Exception when calling ApplicationFiltersApi->delete_single_application_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Application Filter object identifier. | 

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
**400** |  - &#39;id&#39; value must contain values that are greater than or equal to zero - application filter assigned to a security policy cannot be deleted - application filter assigned to a bypass code cannot be deleted |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_filters**
> ApplicationFilterMultiResponse list_application_filters(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)

List Application Filters.

Use this method to retrieve information on all Application Filter objects for the account.  

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
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = fw.ApplicationFiltersApi(api_client)

    try:
        # List Application Filters.
        api_response = api_instance.list_application_filters()
        pprint("The response of ApplicationFiltersApi->list_application_filters:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling ApplicationFiltersApi->list_application_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;.  You can filter by following fields:  | Name                    | type   | Supported Op                | | ----------------------- | ------ | --------------------------- | | name                    | string | !&#x3D;, &#x3D;&#x3D;, ~, !~, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D; |  In addition grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Groupping Operators  |  Allowed sets of parameters that can be groupped in one query:  - name  Example: &#x60;&#x60;&#x60; ?_filter&#x3D;\&quot;((name&#x3D;&#x3D;&#39;app_list1&#39;)or(name~&#39;app_list2&#39;))\&quot; &#x60;&#x60;&#x60;  | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **tfilter** | **str**| Filtering by tags. | [optional] 
 **torder_by** | **str**| Sorting by tags. | [optional] 

### Return type

[**ApplicationFilterMultiResponse**](ApplicationFilterMultiResponse.md)

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

# **read_application_filter**
> ApplicationFilterReadResponse read_application_filter(id, fields=fields, name=name)

Read Application Filter.

Use this method to retrieve information on the specified Application Filter object.  Required: - id 

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
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = fw.ApplicationFiltersApi(api_client)
    id = 56 # int | The Application Filter object identifier.

    try:
        # Read Application Filter.
        api_response = api_instance.read_application_filter(id)
        pprint("The response of ApplicationFiltersApi->read_application_filter:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling ApplicationFiltersApi->read_application_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Application Filter object identifier. | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **name** | **str**| The name of the application filter. | [optional] 

### Return type

[**ApplicationFilterReadResponse**](ApplicationFilterReadResponse.md)

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

# **update_application_filter**
> ApplicationFilterUpdateResponse update_application_filter(id, body)

Update Application Filter.

Use this method to update the specified Application Filter object.  Category filters are content categorization rules that Infoblox Cloud uses to detect and filter specific internet content. Based on your configuration, specific actions such as Allow or Block, will be taken on the detected content. Infoblox Cloud provides the following content categories from which you can build your category filters: Drugs, Risk/Fraud/Crime, Entertainment/Culture, Purchasing, Information/Communication, Business/Services, Information Technology, Lifestyle, Society/Education/Religion, Mature/Violent, Games/Gambling, Pornography/Nudity and Uncategorized. Each of these categories contains sub-categories that further define the respective content. When you configure your category filter, you can add as many sub-categories as you need. You then add the category filter to your security policy and assign the Block action for the filter.  Required: - id - name - criteria 

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
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = fw.ApplicationFiltersApi(api_client)
    id = 56 # int | The Application Filter object identifier.
    body = fw.ApplicationFilter() # ApplicationFilter | The Application Filter object.

    try:
        # Update Application Filter.
        api_response = api_instance.update_application_filter(id, body)
        pprint("The response of ApplicationFiltersApi->update_application_filter:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling ApplicationFiltersApi->update_application_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Application Filter object identifier. | 
 **body** | [**ApplicationFilter**](ApplicationFilter.md)| The Application Filter object. | 

### Return type

[**ApplicationFilterUpdateResponse**](ApplicationFilterUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PUT operation response |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

