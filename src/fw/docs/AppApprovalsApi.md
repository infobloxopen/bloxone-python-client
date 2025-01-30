# fw.AppApprovalsApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_app_approvals**](AppApprovalsApi.md#list_app_approvals) | **GET** /app_approvals | 
[**replace_app_approvals**](AppApprovalsApi.md#replace_app_approvals) | **PUT** /app_approvals | Update Application Approval.
[**update_app_approvals**](AppApprovalsApi.md#update_app_approvals) | **PATCH** /app_approvals | 


# **list_app_approvals**
> AppApprovalMultiResponse list_app_approvals(filter=filter)



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
    api_instance = fw.AppApprovalsApi(api_client)

    try:
        api_response = api_instance.list_app_approvals()
        pprint("The response of AppApprovalsApi->list_app_approvals:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AppApprovalsApi->list_app_approvals: %s\n" % e)
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

# **replace_app_approvals**
> AppApprovalMultiResponse replace_app_approvals(body)

Update Application Approval.

Use this method to update the specified Application Approved object.  Required: an array of approvals - status - app_name  

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
    api_instance = fw.AppApprovalsApi(api_client)
    body = fw.AppApprovalsReplaceRequest() # AppApprovalsReplaceRequest | 

    try:
        # Update Application Approval.
        api_response = api_instance.replace_app_approvals(body)
        pprint("The response of AppApprovalsApi->replace_app_approvals:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AppApprovalsApi->replace_app_approvals: %s\n" % e)
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

# **update_app_approvals**
> AppApprovalMultiResponse update_app_approvals(body)



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
    api_instance = fw.AppApprovalsApi(api_client)
    body = fw.AppApprovalsUpdateRequest() # AppApprovalsUpdateRequest | 

    try:
        api_response = api_instance.update_app_approvals(body)
        pprint("The response of AppApprovalsApi->update_app_approvals:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AppApprovalsApi->update_app_approvals: %s\n" % e)
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

