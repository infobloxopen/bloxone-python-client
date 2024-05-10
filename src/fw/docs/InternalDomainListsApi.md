# fw.InternalDomainListsApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateInternalDomains**](InternalDomainListsApi.md#CreateInternalDomains) | **POST** /internal_domain_lists | Create Internal Domains.
[**DeleteInternalDomains**](InternalDomainListsApi.md#DeleteInternalDomains) | **DELETE** /internal_domain_lists | Delete Internal Domains.
[**DeleteSingleInternalDomains**](InternalDomainListsApi.md#DeleteSingleInternalDomains) | **DELETE** /internal_domain_lists/{id} | Delete Internal Domains.
[**InternalDomainsItemsPartialUpdate**](InternalDomainListsApi.md#InternalDomainsItemsPartialUpdate) | **PATCH** /internal_domain_lists/{id}/items | Patch Internal Domains.
[**ListInternalDomains**](InternalDomainListsApi.md#ListInternalDomains) | **GET** /internal_domain_lists | List Internal Domains.
[**ReadInternalDomains**](InternalDomainListsApi.md#ReadInternalDomains) | **GET** /internal_domain_lists/{id} | Read Internal Domains.
[**UpdateInternalDomains**](InternalDomainListsApi.md#UpdateInternalDomains) | **PUT** /internal_domain_lists/{id} | Update Internal Domains.


# **CreateInternalDomains**
> InternalDomainsCreateResponse CreateInternalDomains(body)

Create Internal Domains.

Use this method to create Internal Domains objects for the account.  The internal domain list is a transport object for reporting gathering internal domains. This feature allows users to configure internal domains lists for specific DFP and ATEP groups. This lists provides the users to create ‘Internal Domains List’ objects with a name, description, and a list of domains/ip/cidr. These lists are referenced by and attached to DFP, and ATEP groups. Once attached to DFP, dfp configuration endpoints will return the values under all associated domain lists as domains.  Once attached to ATEP, atep login endpoint will return the values under all associated lists as internal_domain_lists.   Required: - name - internal_domains  

### Example


```python
import fw
from fw.models.internal_domains import InternalDomains
from fw.models.internal_domains_create_response import InternalDomainsCreateResponse
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
    api_instance = fw.InternalDomainListsApi(api_client)
    body = fw.InternalDomains() # InternalDomains | The Internal Domains object.

    try:
        # Create Internal Domains.
        api_response = api_instance.CreateInternalDomains(body)
        print("The response of InternalDomainListsApi->CreateInternalDomains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalDomainListsApi->CreateInternalDomains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InternalDomains**](InternalDomains.md)| The Internal Domains object. | 

### Return type

[**InternalDomainsCreateResponse**](InternalDomainsCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;description&#39; length cannot exceed 256 characters limit - &#39;internal_domains&#39; must not contain existing Internal domain Lists - &#39;Non-empty lists&#39; |  -  |
**409** |  - &#39;name&#39; value must be unique among internal domains lists belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteInternalDomains**
> DeleteInternalDomains(body)

Delete Internal Domains.

Use this method to delete Internal Domains objects for the account by a given list of internal domain list ids.  The internal domain list is a transport object for reporting gathering internal domains. This feature allows users to configure internal domains lists for specific DFP and ATEP groups. This lists provides the users to create ‘Internal Domains List’ objects with a name, description, and a list of domains/ip/cidr. These lists are referenced by and attached to DFP, and ATEP groups. Once attached to DFP, dfp configuration endpoints will return the values under all associated domain lists as domains.  Once attached to ATEP, atep login endpoint will return the values under all associated lists as internal_domain_lists.  Required: - ids 

### Example


```python
import fw
from fw.models.internal_domains_delete_request import InternalDomainsDeleteRequest
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
    api_instance = fw.InternalDomainListsApi(api_client)
    body = fw.InternalDomainsDeleteRequest() # InternalDomainsDeleteRequest | 

    try:
        # Delete Internal Domains.
        api_instance.DeleteInternalDomains(body)
    except Exception as e:
        print("Exception when calling InternalDomainListsApi->DeleteInternalDomains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InternalDomainsDeleteRequest**](InternalDomainsDeleteRequest.md)|  | 

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
**400** |  - &#39;ids&#39; value must be non-empty - &#39;ids&#39; value must contain unique elements - &#39;ids&#39; value must contain values that are greater than or equal to zero - internal domain list assigned to a endpoint group cannot be deleted  |  -  |
**404** |  - &#39;ids&#39; value must contain existing internal domains identifiers |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteSingleInternalDomains**
> DeleteSingleInternalDomains(id)

Delete Internal Domains.

Use this method to delete Internal Domains objects for the account by a given internal domain list id.  The internal domain list is a transport object for reporting gathering internal domains. This feature allows users to configure internal domains lists for specific DFP and ATEP groups. This lists provides the users to create ‘Internal Domains List’ objects with a name, description, and a list of domains/ip/cidr. These lists are referenced by and attached to DFP, and ATEP groups. Once attached to DFP, dfp configuration endpoints will return the values under all associated domain lists as domains.  Once attached to ATEP, atep login endpoint will return the values under all associated lists as internal_domain_lists.   

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
    api_instance = fw.InternalDomainListsApi(api_client)
    id = 56 # int | The Internal Domains object identifiers.

    try:
        # Delete Internal Domains.
        api_instance.DeleteSingleInternalDomains(id)
    except Exception as e:
        print("Exception when calling InternalDomainListsApi->DeleteSingleInternalDomains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Internal Domains object identifiers. | 

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
**400** |  - &#39;id&#39; value must contain values that are greater than or equal to zero - internal domain list assigned to a endpoint group cannot be deleted  |  -  |
**404** |  - &#39;id&#39; value must contain existing internal domains identifiers |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **InternalDomainsItemsPartialUpdate**
> object InternalDomainsItemsPartialUpdate(id, body)

Patch Internal Domains.

Use this method to insert ot delete items  for a specified Named List object. Note that duplicated items are silently skipped and only new items are appended to the named list. Note that DNSM, TI, Fast Flux, custom lists and DGA lists cannot be updated. Only Internal Domains items can be updated.  The Internal Domains Items represent the list of the FQDN or IPv4 addresses to define whitelists for additional protection. 

### Example


```python
import fw
from fw.models.internal_domains_items import InternalDomainsItems
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
    api_instance = fw.InternalDomainListsApi(api_client)
    id = 56 # int | The Internal Domain List object identifier.
    body = fw.InternalDomainsItems() # InternalDomainsItems | The Internal Domains Items Patch object.

    try:
        # Patch Internal Domains.
        api_response = api_instance.InternalDomainsItemsPartialUpdate(id, body)
        print("The response of InternalDomainListsApi->InternalDomainsItemsPartialUpdate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalDomainListsApi->InternalDomainsItemsPartialUpdate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Internal Domain List object identifier. | 
 **body** | [**InternalDomainsItems**](InternalDomainsItems.md)| The Internal Domains Items Patch object. | 

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
**400** |  - &#39;id&#39; value must be greater than or equal to zero - Invalid domain or IP address or network. |  -  |
**404** |  - &#39;id&#39; value must contain existing named list identifier |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListInternalDomains**
> InternalDomainsMultiResponse ListInternalDomains(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)

List Internal Domains.

Use this method to retrieve information on all Internal Domains objects for the account.  The internal domain list is a transport object for reporting gathering internal domains. This feature allows users to configure internal domains lists for specific DFP and ATEP groups. This lists provides the users to create ‘Internal Domains List’ objects with a name, description, and a list of domains/ip/cidr. These lists are referenced by and attached to DFP, and ATEP groups. Once attached to DFP, dfp configuration endpoints will return the values under all associated domain lists as domains.  Once attached to ATEP, atep login endpoint will return the values under all associated lists as internal_domain_lists.  

### Example


```python
import fw
from fw.models.internal_domains_multi_response import InternalDomainsMultiResponse
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
    api_instance = fw.InternalDomainListsApi(api_client)
    filter = 'filter_example' # str | A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name               | type   | Supported Op                | | ------------------ | ------ | --------------------------- | | id                 | int32  | !=, ==, >, <, <=, >=        | | name               | string | !=, ==, ~, !~, >, <, <=, >= | | description        | string | !=, ==, ~, !~, >, <, <=, >= | | items              | string | ~, !~                       | | is_default         | bool   | !=, ==                      |  In addition grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Grouping Operators  |  Example: ``` ?_filter=\"((name=='internal_dom_a')or(name~'internal_dom_b'))\" ```  (optional)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
    limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
    page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
    tfilter = 'tfilter_example' # str | Filtering by tags. (optional)
    torder_by = 'torder_by_example' # str | Sorting by tags. (optional)

    try:
        # List Internal Domains.
        api_response = api_instance.ListInternalDomains(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)
        print("The response of InternalDomainListsApi->ListInternalDomains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalDomainListsApi->ListInternalDomains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;.  You can filter by following fields:  | Name               | type   | Supported Op                | | ------------------ | ------ | --------------------------- | | id                 | int32  | !&#x3D;, &#x3D;&#x3D;, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D;        | | name               | string | !&#x3D;, &#x3D;&#x3D;, ~, !~, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D; | | description        | string | !&#x3D;, &#x3D;&#x3D;, ~, !~, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D; | | items              | string | ~, !~                       | | is_default         | bool   | !&#x3D;, &#x3D;&#x3D;                      |  In addition grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Grouping Operators  |  Example: &#x60;&#x60;&#x60; ?_filter&#x3D;\&quot;((name&#x3D;&#x3D;&#39;internal_dom_a&#39;)or(name~&#39;internal_dom_b&#39;))\&quot; &#x60;&#x60;&#x60;  | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **tfilter** | **str**| Filtering by tags. | [optional] 
 **torder_by** | **str**| Sorting by tags. | [optional] 

### Return type

[**InternalDomainsMultiResponse**](InternalDomainsMultiResponse.md)

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

# **ReadInternalDomains**
> InternalDomainsReadResponse ReadInternalDomains(id, fields=fields, name=name, offset=offset, limit=limit, page_token=page_token)

Read Internal Domains.

Use this method to read Internal Domains objects for the account by a internal domain list id.  The internal domain list is a transport object for reporting gathering internal domains. This feature allows users to configure internal domains lists for specific DFP and ATEP groups. This lists provides the users to create ‘Internal Domains List’ objects with a name, description, and a list of domains/ip/cidr. These lists are referenced by and attached to DFP, and ATEP groups. Once attached to DFP, dfp configuration endpoints will return the values under all associated domain lists as domains.  Once attached to ATEP, atep login endpoint will return the values under all associated lists as internal_domain_lists. 

### Example


```python
import fw
from fw.models.internal_domains_read_response import InternalDomainsReadResponse
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
    api_instance = fw.InternalDomainListsApi(api_client)
    id = 56 # int | The Internal Domains object identifier.
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    name = 'name_example' # str | The name of InternalDomains object. Used if id==0. (optional)
    offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
    limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
    page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)

    try:
        # Read Internal Domains.
        api_response = api_instance.ReadInternalDomains(id, fields=fields, name=name, offset=offset, limit=limit, page_token=page_token)
        print("The response of InternalDomainListsApi->ReadInternalDomains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalDomainListsApi->ReadInternalDomains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Internal Domains object identifier. | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **name** | **str**| The name of InternalDomains object. Used if id&#x3D;&#x3D;0. | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 

### Return type

[**InternalDomainsReadResponse**](InternalDomainsReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |
**404** |  - &#39;id&#39; value must contain existing internal domain lists identifier |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateInternalDomains**
> InternalDomainsUpdateResponse UpdateInternalDomains(id, body)

Update Internal Domains.

Use this method to update Internal Domains objects for the account by a internal domain list id.  The internal domain list is a transport object for reporting gathering internal domains. This feature allows users to configure internal domains lists for specific DFP and ATEP groups. This lists provides the users to create ‘Internal Domains List’ objects with a name, description, and a list of domains/ip/cidr. These lists are referenced by and attached to DFP, and ATEP groups. Once attached to DFP, dfp configuration endpoints will return the values under all associated domain lists as domains.  Once attached to ATEP, atep login endpoint will return the values under all associated lists as internal_domain_lists.  Required: - name - internal_domains 

### Example


```python
import fw
from fw.models.internal_domains import InternalDomains
from fw.models.internal_domains_update_response import InternalDomainsUpdateResponse
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
    api_instance = fw.InternalDomainListsApi(api_client)
    id = 56 # int | The Internal Domain object identifier.
    body = fw.InternalDomains() # InternalDomains | The Internal Domains object.

    try:
        # Update Internal Domains.
        api_response = api_instance.UpdateInternalDomains(id, body)
        print("The response of InternalDomainListsApi->UpdateInternalDomains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalDomainListsApi->UpdateInternalDomains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Internal Domain object identifier. | 
 **body** | [**InternalDomains**](InternalDomains.md)| The Internal Domains object. | 

### Return type

[**InternalDomainsUpdateResponse**](InternalDomainsUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PUT operation response |  -  |
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;description&#39; length cannot exceed 256 characters limit - &#39;internal_domains&#39; must contain existing internal domain Lists - &#39;internal_domains&#39; values is not a domain, cidr, or ip |  -  |
**404** |  - &#39;id&#39; value must contain existing internal domains list identifier  |  -  |
**409** |  - &#39;name&#39; value must be unique among internal domains belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

