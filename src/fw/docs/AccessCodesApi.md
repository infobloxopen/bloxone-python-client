# fw.AccessCodesApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_code**](AccessCodesApi.md#create_access_code) | **POST** /access_codes | Create Access Codes
[**delete_access_codes**](AccessCodesApi.md#delete_access_codes) | **DELETE** /access_codes | Delete Access Codes
[**delete_single_access_codes**](AccessCodesApi.md#delete_single_access_codes) | **DELETE** /access_codes/{access_key} | Delete Access Code By ID
[**list_access_codes**](AccessCodesApi.md#list_access_codes) | **GET** /access_codes | List Access Codes
[**read_access_code**](AccessCodesApi.md#read_access_code) | **GET** /access_codes/{access_key} | Read Access Codes
[**update_access_code**](AccessCodesApi.md#update_access_code) | **PUT** /access_codes/{payload.access_key} | Update Access Codes


# **create_access_code**
> AccessCodeCreateResponse create_access_code(body)

Create Access Codes

Use this method to create the Bypass Code corresponding to the security rules passed. It's an atomic operation. It should create all the security rules and create the policy and bypass codes, or do nothing if any of them fails.  Required: - name - rules - activation - expiration    

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
    api_instance = fw.AccessCodesApi(api_client)
    body = fw.AccessCode() # AccessCode | The Bypass Code object.

    try:
        # Create Access Codes
        api_response = api_instance.create_access_code(body)
        pprint("The response of AccessCodesApi->create_access_code:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AccessCodesApi->create_access_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessCode**](AccessCode.md)| The Bypass Code object. | 

### Return type

[**AccessCodeCreateResponse**](AccessCodeCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;description&#39; length cannot exceed 256 characters limit - Expiration date must be after activation date - Cannot enter expired Bypass Code |  -  |
**404** |  - Threat Feed and TI rules must contain existing threat feeds and TI lists - Custom Redirect rules must contain existing Custom Redirect - Custom List rules must contain existing Custom List |  -  |
**409** |  - &#39;name&#39; value must be unique among bypass codes belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_codes**
> delete_access_codes(body)

Delete Access Codes

Use this method to delete Bypass Code objects. Deletion of multiple bypass codes is an all-or-nothing operation (if any of the specified bypass codes cannot be deleted then none of the specified bypass codes will be deleted).  Required: - ids  

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
    api_instance = fw.AccessCodesApi(api_client)
    body = fw.AccessCodeDeleteRequest() # AccessCodeDeleteRequest | 

    try:
        # Delete Access Codes
        api_instance.delete_access_codes(body)
    except Exception as e:
        pprint("Exception when calling AccessCodesApi->delete_access_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessCodeDeleteRequest**](AccessCodeDeleteRequest.md)|  | 

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
**400** |  - &#39;ids&#39; value must contain unique elements - &#39;ids&#39; value must contain existing bypass code key - Cannot delete bypass code assigned to policy |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_single_access_codes**
> delete_single_access_codes(access_key)

Delete Access Code By ID

Use this method to delete Bypass Code object.  

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
    api_instance = fw.AccessCodesApi(api_client)
    access_key = 'access_key_example' # str | The Bypass Code identifier.

    try:
        # Delete Access Code By ID
        api_instance.delete_single_access_codes(access_key)
    except Exception as e:
        pprint("Exception when calling AccessCodesApi->delete_single_access_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | **str**| The Bypass Code identifier. | 

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
**400** |  - &#39;id&#39; value must contain existing bypass code key - Cannot delete bypass code assigned to policy |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_access_codes**
> AccessCodeMultiResponse list_access_codes(filter=filter, offset=offset, limit=limit, page_token=page_token)

List Access Codes

Use this method to retrieve a collection of Bypass Code objects.  

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
    api_instance = fw.AccessCodesApi(api_client)

    try:
        # List Access Codes
        api_response = api_instance.list_access_codes()
        pprint("The response of AccessCodesApi->list_access_codes:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AccessCodesApi->list_access_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;.  You can filter by following fields:  | Name               | type   | Supported Op                | | ------------------ | ------ | --------------------------- | | access_key         | string | !&#x3D;, &#x3D;&#x3D;, ~, !~, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D; | | name               | string | !&#x3D;, &#x3D;&#x3D;, ~, !~, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D; | | description        | string | !&#x3D;, &#x3D;&#x3D;, ~, !~, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D; | | security_policy_id | int32  | !&#x3D;, &#x3D;&#x3D;, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D;        |  In addition, grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Groupping Operators  |  Example: &#x60;&#x60;&#x60; ?_filter&#x3D;\&quot;((name&#x3D;&#x3D;&#39;acc_code&#39;)or(name~&#39;key&#39;))and(security_policy_id!&#x3D;32)\&quot; &#x60;&#x60;&#x60;  | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 

### Return type

[**AccessCodeMultiResponse**](AccessCodeMultiResponse.md)

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

# **read_access_code**
> AccessCodeReadResponse read_access_code(access_key, name=name)

Read Access Codes

Use this method to retrieve the Bypass Code by key.  

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
    api_instance = fw.AccessCodesApi(api_client)
    access_key = 'access_key_example' # str | The Bypass Code identifier.

    try:
        # Read Access Codes
        api_response = api_instance.read_access_code(access_key)
        pprint("The response of AccessCodesApi->read_access_code:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AccessCodesApi->read_access_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | **str**| The Bypass Code identifier. | 
 **name** | **str**| The Bypass Code name. | [optional] 

### Return type

[**AccessCodeReadResponse**](AccessCodeReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |
**404** |  - &#39;access_codes&#39; value must contain existing bypass code key |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_code**
> AccessCodeUpdateResponse update_access_code(payload_access_key, body)

Update Access Codes

Use this method to update the Bypass Code corresponding to the security rules passed. It's an atomic operation. It should delete existing security rules and create all the new security rules for the bypass code, or do nothing if any of them fails.  Required: - name - rules - dfps - network_lists - roaming_device_groups    

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
    api_instance = fw.AccessCodesApi(api_client)
    payload_access_key = 'payload_access_key_example' # str | Auto generated unique Bypass Code value
    body = fw.AccessCode() # AccessCode | The Bypass Code object.

    try:
        # Update Access Codes
        api_response = api_instance.update_access_code(payload_access_key, body)
        pprint("The response of AccessCodesApi->update_access_code:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AccessCodesApi->update_access_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload_access_key** | **str**| Auto generated unique Bypass Code value | 
 **body** | [**AccessCode**](AccessCode.md)| The Bypass Code object. | 

### Return type

[**AccessCodeUpdateResponse**](AccessCodeUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PUT operation response |  -  |
**400** |  - &#39;name&#39; length cannot exceed 256 characters limit - &#39;description&#39; length cannot exceed 256 characters limit - Expiration date must be after activation date - Cannot enter expired Bypass Code |  -  |
**404** |  - Threat Feed and TI rules must contain existing threat feeds and TI lists - Custom Redirect rules must contain existing Custom Redirect - Custom List rules must contain existing Custom List |  -  |
**409** |  - &#39;name&#39; value must be unique among bypass codes belonging to the same account |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

