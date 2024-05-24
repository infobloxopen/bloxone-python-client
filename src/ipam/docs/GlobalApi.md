# ipam.GlobalApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read**](GlobalApi.md#read) | **GET** /dhcp/global | Retrieve the global configuration.
[**read_by_id**](GlobalApi.md#read_by_id) | **GET** /dhcp/global/{id} | Retrieve the global configuration.
[**update**](GlobalApi.md#update) | **PATCH** /dhcp/global | Update the global configuration.
[**update_by_id**](GlobalApi.md#update_by_id) | **PATCH** /dhcp/global/{id} | Update the global configuration.


# **read**
> ReadGlobalResponse read(fields=fields)

Retrieve the global configuration.

Use this method to retrieve the __Global__ configuration object. The service operates on single __Global__ (_dhcp/global_) object that represents parent configuration settings for inheritance.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.read_global_response import ReadGlobalResponse
from ipam.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ipam.Configuration(
    host = "http://csp.infoblox.com/api/ddi/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ipam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipam.GlobalApi(api_client)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

    try:
        # Retrieve the global configuration.
        api_response = api_instance.read(fields=fields)
        print("The response of GlobalApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**ReadGlobalResponse**](ReadGlobalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_by_id**
> ReadGlobalResponse read_by_id(id, fields=fields)

Retrieve the global configuration.

Use this method to retrieve the __Global__ configuration object. The service operates on single __Global__ (_dhcp/global_) object that represents parent configuration settings for inheritance.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.read_global_response import ReadGlobalResponse
from ipam.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ipam.Configuration(
    host = "http://csp.infoblox.com/api/ddi/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ipam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipam.GlobalApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

    try:
        # Retrieve the global configuration.
        api_response = api_instance.read_by_id(id, fields=fields)
        print("The response of GlobalApi->read_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApi->read_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**ReadGlobalResponse**](ReadGlobalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> UpdateGlobalResponse update(body)

Update the global configuration.

Use this method to update the __Global__ configuration object. The service operates on single __Global__ (_dhcp/global_) object that represents parent configuration settings for inheritance.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.dhcp_global import DHCPGlobal
from ipam.models.update_global_response import UpdateGlobalResponse
from ipam.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ipam.Configuration(
    host = "http://csp.infoblox.com/api/ddi/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ipam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipam.GlobalApi(api_client)
    body = ipam.DHCPGlobal() # DHCPGlobal | 

    try:
        # Update the global configuration.
        api_response = api_instance.update(body)
        print("The response of GlobalApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DHCPGlobal**](DHCPGlobal.md)|  | 

### Return type

[**UpdateGlobalResponse**](UpdateGlobalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PATCH operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_by_id**
> UpdateGlobalResponse update_by_id(id, body)

Update the global configuration.

Use this method to update the __Global__ configuration object. The service operates on single __Global__ (_dhcp/global_) object that represents parent configuration settings for inheritance.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.dhcp_global import DHCPGlobal
from ipam.models.update_global_response import UpdateGlobalResponse
from ipam.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ipam.Configuration(
    host = "http://csp.infoblox.com/api/ddi/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ipam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipam.GlobalApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = ipam.DHCPGlobal() # DHCPGlobal | 

    try:
        # Update the global configuration.
        api_response = api_instance.update_by_id(id, body)
        print("The response of GlobalApi->update_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApi->update_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**DHCPGlobal**](DHCPGlobal.md)|  | 

### Return type

[**UpdateGlobalResponse**](UpdateGlobalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PATCH operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

