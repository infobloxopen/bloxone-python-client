# fw.ContentCategoriesApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ListContentCategories**](ContentCategoriesApi.md#ListContentCategories) | **GET** /content_categories | List Content Categories.


# **ListContentCategories**
> ContentCategoryMultiResponse ListContentCategories(fields=fields)

List Content Categories.

Use this method to retrieve information on all Content Category objects for the account.  The Content Category object represents a specific internet content and used to configure category filters. Based on your configuration, specific actions such as Allow or Block, will be taken on the detected content. BloxOne Cloud provides the following content categories from which you can build your category filters: Drugs, Risk/Fraud/Crime, Entertainment/Culture, Purchasing, Information/Communication, Business/Services, Information Technology, Lifestyle, Society/Education/Religion, Mature/Violent, Games/Gambling, Pornography/Nudity and Uncategorized. Each of these categories contains sub-categories that further define the respective content. 

### Example


```python
import fw
from fw.models.content_category_multi_response import ContentCategoryMultiResponse
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
    api_instance = fw.ContentCategoriesApi(api_client)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

    try:
        # List Content Categories.
        api_response = api_instance.ListContentCategories(fields=fields)
        print("The response of ContentCategoriesApi->ListContentCategories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentCategoriesApi->ListContentCategories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**ContentCategoryMultiResponse**](ContentCategoryMultiResponse.md)

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

