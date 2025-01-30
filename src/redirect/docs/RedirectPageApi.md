# redirect.RedirectPageApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_redirect_page**](RedirectPageApi.md#read_redirect_page) | **GET** /redirect_page | Read Redirect Page.
[**update_redirect_page**](RedirectPageApi.md#update_redirect_page) | **PUT** /redirect_page | Update Redirect Page.


# **read_redirect_page**
> RedirectPageReadResponse read_redirect_page(filter=filter, fields=fields)

Read Redirect Page.

Use this method to retrieve the Redirect Page object.  When blocking users from accessing certain domains, you can redirect them to a page that delivers a default message about the action. You can also set a redirect page of your own or customize the redirect message. 

### Example

```python
import os
from pprint import pprint

import redirect

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
    api_instance = redirect.RedirectPageApi(api_client)

    try:
        # Read Redirect Page.
        api_response = api_instance.read_redirect_page()
        pprint("The response of RedirectPageApi->read_redirect_page:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling RedirectPageApi->read_redirect_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**RedirectPageReadResponse**](RedirectPageReadResponse.md)

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

# **update_redirect_page**
> RedirectPageUpdateResponse update_redirect_page(body)

Update Redirect Page.

Use this method to update the Redirect Page object.  When blocking users from accessing certain domains, you can redirect them to a page that delivers a default message about the action. You can also set a redirect page of your own or customize the redirect message.  Required: - type 

### Example

```python
import os
from pprint import pprint

import redirect

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
    api_instance = redirect.RedirectPageApi(api_client)
    body = redirect.UpdateRedirectPagePayload() # UpdateRedirectPagePayload | The Redirect Page object.

    try:
        # Update Redirect Page.
        api_response = api_instance.update_redirect_page(body)
        pprint("The response of RedirectPageApi->update_redirect_page:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling RedirectPageApi->update_redirect_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRedirectPagePayload**](UpdateRedirectPagePayload.md)| The Redirect Page object. | 

### Return type

[**RedirectPageUpdateResponse**](RedirectPageUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PUT operation response |  -  |
**400** |  - &#39;type&#39; value must contain valid redirect page type that is &#39;custom&#39; or &#39;default&#39; - &#39;content&#39; length cannot exceed 262144 characters limit - &#39;redirect_ip_address&#39; must contain valid IPv4 address |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

