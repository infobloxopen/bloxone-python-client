# fw.NamedListItemsApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_named_list_items**](NamedListItemsApi.md#delete_named_list_items) | **DELETE** /named_lists/{id}/items | Delete Named List Items.
[**insert_or_replace_named_list_items**](NamedListItemsApi.md#insert_or_replace_named_list_items) | **POST** /named_lists/{id}/items | Insert Named List Items.
[**named_list_items_partial_update**](NamedListItemsApi.md#named_list_items_partial_update) | **PATCH** /named_lists/{id}/items | Partial Update Named List Items.


# **delete_named_list_items**
> delete_named_list_items(id, body)

Delete Named List Items.

Use this method to remove items from a specified Named List object. Note that duplicated items are silently skipped and only new items are appended to the named list. Note that DNSM, TI, Fast Flux and DGA lists cannot be updated. Only Custom List items can be deleted.  The Custom List Items represent the list of the FQDN or IPv4 or IPv6 addresses to define whitelists and blacklists for additional protection.  Required: - items 

### Example


```python
import fw
from fw.models.named_list_items_delete_request import NamedListItemsDeleteRequest
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
    api_instance = fw.NamedListItemsApi(api_client)
    id = 56 # int | The Named List object identifier.
    body = fw.NamedListItemsDeleteRequest() # NamedListItemsDeleteRequest | 

    try:
        # Delete Named List Items.
        api_instance.delete_named_list_items(id, body)
    except Exception as e:
        print("Exception when calling NamedListItemsApi->delete_named_list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Named List object identifier. | 
 **body** | [**NamedListItemsDeleteRequest**](NamedListItemsDeleteRequest.md)|  | 

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
**400** |  - &#39;id&#39; value must be greater than or equal to zero - &#39;items&#39; value must contain either valid domain names or IPv4 or IPv6 or network addresses. - &#39;items&#39; value must contain existing values for a specified named list |  -  |
**404** |  - &#39;id&#39; value must contain existing custom list identifier |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_or_replace_named_list_items**
> NamedListItemsInsertOrUpdateResponse insert_or_replace_named_list_items(id, body)

Insert Named List Items.

Use this method to update existing items with new ones for a specified Named List object. Note that duplicated items are silently skipped and only new items are appended to the named list. Note that DNSM, TI, Fast Flux and DGA lists cannot be updated. Only Custom List items can be updated.  The Custom List Items represent the list of the FQDN or IPv4 addresses to define whitelists and blacklists for additional protection. 

### Example


```python
import fw
from fw.models.named_list_items_insert_or_update import NamedListItemsInsertOrUpdate
from fw.models.named_list_items_insert_or_update_response import NamedListItemsInsertOrUpdateResponse
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
    api_instance = fw.NamedListItemsApi(api_client)
    id = 56 # int | The Named List object identifier.
    body = fw.NamedListItemsInsertOrUpdate() # NamedListItemsInsertOrUpdate | NamedListItemsInsertOrUpdate object

    try:
        # Insert Named List Items.
        api_response = api_instance.insert_or_replace_named_list_items(id, body)
        print("The response of NamedListItemsApi->insert_or_replace_named_list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamedListItemsApi->insert_or_replace_named_list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Named List object identifier. | 
 **body** | [**NamedListItemsInsertOrUpdate**](NamedListItemsInsertOrUpdate.md)| NamedListItemsInsertOrUpdate object | 

### Return type

[**NamedListItemsInsertOrUpdateResponse**](NamedListItemsInsertOrUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |
**400** |  - &#39;id&#39; value must be greater than or equal to zero - &#39;items&#39; value must contain either valid domain names or IPv4 or IPv6 or network addresses. |  -  |
**404** |  - &#39;id&#39; value must contain existing named list identifier |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **named_list_items_partial_update**
> object named_list_items_partial_update(id, body)

Partial Update Named List Items.

Use this method to insert ot delete items  for a specified Named List object. Note that duplicated items are silently skipped and only new items are appended to the named list. Note that DNSM, TI, Fast Flux and DGA lists cannot be updated. Only Custom List items can be updated.  The Custom List Items represent the list of the FQDN or IPv4 addresses to define whitelists and blacklists for additional protection. 

### Example


```python
import fw
from fw.models.named_list_items_partial_update import NamedListItemsPartialUpdate
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
    api_instance = fw.NamedListItemsApi(api_client)
    id = 56 # int | The Named List object identifier.
    body = fw.NamedListItemsPartialUpdate() # NamedListItemsPartialUpdate | NamedListItemsPartialUpdate object

    try:
        # Partial Update Named List Items.
        api_response = api_instance.named_list_items_partial_update(id, body)
        print("The response of NamedListItemsApi->named_list_items_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamedListItemsApi->named_list_items_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Named List object identifier. | 
 **body** | [**NamedListItemsPartialUpdate**](NamedListItemsPartialUpdate.md)| NamedListItemsPartialUpdate object | 

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
**400** |  - &#39;id&#39; value must be greater than or equal to zero - &#39;items&#39; value must contain either valid domain names or IPv4 or network addresses. |  -  |
**404** |  - &#39;id&#39; value must contain existing named list identifier |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

