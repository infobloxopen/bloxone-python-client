# redirect.CustomRedirectsApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_redirect**](CustomRedirectsApi.md#create_custom_redirect) | **POST** /custom_redirects | Create Custom Redirect.
[**delete_custom_redirect**](CustomRedirectsApi.md#delete_custom_redirect) | **DELETE** /custom_redirects | Delete Custom Redirect.
[**delete_single_custom_redirect**](CustomRedirectsApi.md#delete_single_custom_redirect) | **DELETE** /custom_redirects/{id} | Delete Custom Redirect By Id.
[**list_custom_redirect**](CustomRedirectsApi.md#list_custom_redirect) | **GET** /custom_redirects | List Custom Redirects.
[**read_custom_redirect**](CustomRedirectsApi.md#read_custom_redirect) | **GET** /custom_redirects/{id} | Read Custom Redirect.
[**update_custom_redirect**](CustomRedirectsApi.md#update_custom_redirect) | **PUT** /custom_redirects/{id} | Update Custom Redirect.


# **create_custom_redirect**
> CustomRedirectCreateResponse create_custom_redirect(body)

Create Custom Redirect.

Use this method to create a Custom Redirect object.  You can configure BloxOne Cloud to redirect traffic to the Infoblox redirect page or a custom redirect destination. BloxOne Cloud allows you to apply multiple redirect actions and integrate BloxOne Cloud with third-party proxies, secure web gateways, blackholes, honeypots and sinkhole solutions.  Required: - name - data 

### Example


```python
import redirect
from redirect.models.custom_redirect import CustomRedirect
from redirect.models.custom_redirect_create_response import CustomRedirectCreateResponse
from redirect.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = redirect.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with redirect.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = redirect.CustomRedirectsApi(api_client)
    body = redirect.CustomRedirect() # CustomRedirect | The Custom Redirect object.

    try:
        # Create Custom Redirect.
        api_response = api_instance.create_custom_redirect(body)
        print("The response of CustomRedirectsApi->create_custom_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomRedirectsApi->create_custom_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomRedirect**](CustomRedirect.md)| The Custom Redirect object. | 

### Return type

[**CustomRedirectCreateResponse**](CustomRedirectCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;description&#39; length cannot exceed 256 characters limit - &#39;data&#39; must contain a valid IPv4 address or domain name |  -  |
**409** |  - &#39;name&#39; value must be unique among named lists belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_redirect**
> delete_custom_redirect(body)

Delete Custom Redirect.

Use this method to delete Custom Redirect objects. Deletion of multiple lists is an all-or-nothing operation (if any of the specified lists can not be deleted then none of the specified lists will be deleted).  You can configure BloxOne Cloud to redirect traffic to the Infoblox redirect page or a custom redirect destination. BloxOne Cloud allows you to apply multiple redirect actions and integrate BloxOne Cloud with third-party proxies, secure web gateways, blackholes, honeypots and sinkhole solutions.  Required: - ids 

### Example


```python
import redirect
from redirect.models.custom_redirect_delete_request import CustomRedirectDeleteRequest
from redirect.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = redirect.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with redirect.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = redirect.CustomRedirectsApi(api_client)
    body = redirect.CustomRedirectDeleteRequest() # CustomRedirectDeleteRequest | 

    try:
        # Delete Custom Redirect.
        api_instance.delete_custom_redirect(body)
    except Exception as e:
        print("Exception when calling CustomRedirectsApi->delete_custom_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomRedirectDeleteRequest**](CustomRedirectDeleteRequest.md)|  | 

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
**400** |  - &#39;ids&#39; value must be non-empty - &#39;ids&#39; value must contain unique elements - &#39;ids&#39; value must contain values that are greater than or equal to zero - custom redirects assigned to a security policy cannot be deleted - &#39;ids&#39; value must contain existing custom redirect identifiers |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_single_custom_redirect**
> delete_single_custom_redirect(id)

Delete Custom Redirect By Id.

Use this method to delete Custom Redirect object.  You can configure BloxOne Cloud to redirect traffic to the Infoblox redirect page or a custom redirect destination. BloxOne Cloud allows you to apply multiple redirect actions and integrate BloxOne Cloud with third-party proxies, secure web gateways, blackholes, honeypots and sinkhole solutions. 

### Example


```python
import redirect
from redirect.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = redirect.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with redirect.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = redirect.CustomRedirectsApi(api_client)
    id = 56 # int | The Custom Redirect object identifier.

    try:
        # Delete Custom Redirect By Id.
        api_instance.delete_single_custom_redirect(id)
    except Exception as e:
        print("Exception when calling CustomRedirectsApi->delete_single_custom_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Custom Redirect object identifier. | 

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
**400** |  - &#39;id&#39; value must contain values that are greater than or equal to zero - &#39;ids&#39; value must contain existing custom redirect identifiers - custom redirects assigned to a security policy cannot be deleted |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_redirect**
> CustomRedirectMultiResponse list_custom_redirect(fields=fields, filter=filter)

List Custom Redirects.

Use this method to retrieve information on all Custom Redirect objects for the account.  You can configure BloxOne Cloud to redirect traffic to the Infoblox redirect page or a custom redirect destination. BloxOne Cloud allows you to apply multiple redirect actions and integrate BloxOne Cloud with third-party proxies, secure web gateways, blackholes, honeypots and sinkhole solutions. 

### Example


```python
import redirect
from redirect.models.custom_redirect_multi_response import CustomRedirectMultiResponse
from redirect.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = redirect.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with redirect.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = redirect.CustomRedirectsApi(api_client)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)

    try:
        # List Custom Redirects.
        api_response = api_instance.list_custom_redirect(fields=fields, filter=filter)
        print("The response of CustomRedirectsApi->list_custom_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomRedirectsApi->list_custom_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 

### Return type

[**CustomRedirectMultiResponse**](CustomRedirectMultiResponse.md)

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

# **read_custom_redirect**
> CustomRedirectReadResponse read_custom_redirect(id, fields=fields, name=name)

Read Custom Redirect.

Use this method to retrieve information on the specified Custom Redirect object.  You can configure BloxOne Cloud to redirect traffic to the Infoblox redirect page or a custom redirect destination. BloxOne Cloud allows you to apply multiple redirect actions and integrate BloxOne Cloud with third-party proxies, secure web gateways, blackholes, honeypots and sinkhole solutions. 

### Example


```python
import redirect
from redirect.models.custom_redirect_read_response import CustomRedirectReadResponse
from redirect.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = redirect.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with redirect.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = redirect.CustomRedirectsApi(api_client)
    id = 56 # int | The Custom Redirect object identifier.
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    name = 'name_example' # str | The name of the custom redirect. May be used if id==0. (optional)

    try:
        # Read Custom Redirect.
        api_response = api_instance.read_custom_redirect(id, fields=fields, name=name)
        print("The response of CustomRedirectsApi->read_custom_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomRedirectsApi->read_custom_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Custom Redirect object identifier. | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **name** | **str**| The name of the custom redirect. May be used if id&#x3D;&#x3D;0. | [optional] 

### Return type

[**CustomRedirectReadResponse**](CustomRedirectReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |
**404** |  - &#39;id&#39; value must contain existing custom redirect identifier |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_redirect**
> CustomRedirectUpdateResponse update_custom_redirect(id, body)

Update Custom Redirect.

Use this method to update a specified Custom Redirect object.  You can configure BloxOne Cloud to redirect traffic to the Infoblox redirect page or a custom redirect destination. BloxOne Cloud allows you to apply multiple redirect actions and integrate BloxOne Cloud with third-party proxies, secure web gateways, blackholes, honeypots and sinkhole solutions.  Required: - name - data 

### Example


```python
import redirect
from redirect.models.custom_redirect import CustomRedirect
from redirect.models.custom_redirect_update_response import CustomRedirectUpdateResponse
from redirect.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = redirect.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with redirect.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = redirect.CustomRedirectsApi(api_client)
    id = 56 # int | The Custom Redirect object identifier.
    body = redirect.CustomRedirect() # CustomRedirect | The Custom Redirect object.

    try:
        # Update Custom Redirect.
        api_response = api_instance.update_custom_redirect(id, body)
        print("The response of CustomRedirectsApi->update_custom_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomRedirectsApi->update_custom_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Custom Redirect object identifier. | 
 **body** | [**CustomRedirect**](CustomRedirect.md)| The Custom Redirect object. | 

### Return type

[**CustomRedirectUpdateResponse**](CustomRedirectUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PUT operation response |  -  |
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;description&#39; length cannot exceed 256 characters limit - &#39;data&#39; must contain a valid IPv4 address or domain name |  -  |
**404** |  - &#39;id&#39; value must contain existing custom redirect identifier |  -  |
**409** |  - &#39;name&#39; value must be unique among named lists belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

