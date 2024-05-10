# fw.AppApprovalsApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ListAppApprovals**](AppApprovalsApi.md#ListAppApprovals) | **GET** /app_approvals | 
[**ReplaceAppApprovals**](AppApprovalsApi.md#ReplaceAppApprovals) | **PUT** /app_approvals | Update Application Approval.
[**UpdateAppApprovals**](AppApprovalsApi.md#UpdateAppApprovals) | **PATCH** /app_approvals | 


# **ListAppApprovals**
> AppApprovalMultiResponse ListAppApprovals(filter=filter)



### Example


```python
import fw
from fw.models.app_approval_multi_response import AppApprovalMultiResponse
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
    api_instance = fw.AppApprovalsApi(api_client)
    filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)

    try:
        api_response = api_instance.ListAppApprovals(filter=filter)
        print("The response of AppApprovalsApi->ListAppApprovals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApprovalsApi->ListAppApprovals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 

### Return type

[**AppApprovalMultiResponse**](AppApprovalMultiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ReplaceAppApprovals**
> AppApprovalMultiResponse ReplaceAppApprovals(body)

Update Application Approval.

Use this method to update the specified Application Approved object.  Required: an array of approvals - status - app_name  

### Example


```python
import fw
from fw.models.app_approval_multi_response import AppApprovalMultiResponse
from fw.models.app_approvals_replace_request import AppApprovalsReplaceRequest
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
    api_instance = fw.AppApprovalsApi(api_client)
    body = fw.AppApprovalsReplaceRequest() # AppApprovalsReplaceRequest | 

    try:
        # Update Application Approval.
        api_response = api_instance.ReplaceAppApprovals(body)
        print("The response of AppApprovalsApi->ReplaceAppApprovals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApprovalsApi->ReplaceAppApprovals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppApprovalsReplaceRequest**](AppApprovalsReplaceRequest.md)|  | 

### Return type

[**AppApprovalMultiResponse**](AppApprovalMultiResponse.md)

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

# **UpdateAppApprovals**
> AppApprovalMultiResponse UpdateAppApprovals(body)



### Example


```python
import fw
from fw.models.app_approval_multi_response import AppApprovalMultiResponse
from fw.models.app_approvals_update_request import AppApprovalsUpdateRequest
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
    api_instance = fw.AppApprovalsApi(api_client)
    body = fw.AppApprovalsUpdateRequest() # AppApprovalsUpdateRequest | 

    try:
        api_response = api_instance.UpdateAppApprovals(body)
        print("The response of AppApprovalsApi->UpdateAppApprovals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApprovalsApi->UpdateAppApprovals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppApprovalsUpdateRequest**](AppApprovalsUpdateRequest.md)|  | 

### Return type

[**AppApprovalMultiResponse**](AppApprovalMultiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PATCH operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

