# dns_config.GlobalApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Read**](GlobalApi.md#Read) | **GET** /dns/global | Read the Global configuration object.
[**Read2**](GlobalApi.md#Read2) | **GET** /dns/global/{id} | Read the Global configuration object.
[**Update**](GlobalApi.md#Update) | **PATCH** /dns/global | Update the Global configuration object.
[**Update2**](GlobalApi.md#Update2) | **PATCH** /dns/global/{id} | Update the Global configuration object.


# **Read**
> ReadGlobalResponse Read(fields=fields)

Read the Global configuration object.

Use this method to read the Global configuration object. Service operates on Global singleton object that represents parent configuration settings for inheritance.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dns_config
from dns_config.models.read_global_response import ReadGlobalResponse
from dns_config.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dns_config.Configuration(
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
with dns_config.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dns_config.GlobalApi(api_client)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

    try:
        # Read the Global configuration object.
        api_response = api_instance.Read(fields=fields)
        print("The response of GlobalApi->Read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApi->Read: %s\n" % e)
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

# **Read2**
> ReadGlobalResponse Read2(id, fields=fields)

Read the Global configuration object.

Use this method to read the Global configuration object. Service operates on Global singleton object that represents parent configuration settings for inheritance.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dns_config
from dns_config.models.read_global_response import ReadGlobalResponse
from dns_config.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dns_config.Configuration(
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
with dns_config.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dns_config.GlobalApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

    try:
        # Read the Global configuration object.
        api_response = api_instance.Read2(id, fields=fields)
        print("The response of GlobalApi->Read2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApi->Read2: %s\n" % e)
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

# **Update**
> UpdateGlobalResponse Update(body)

Update the Global configuration object.

Use this method to update the Global configuration object. Service operates on Global singleton object that represents parent configuration settings for inheritance.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dns_config
from dns_config.models.dns_global import DNSGlobal
from dns_config.models.update_global_response import UpdateGlobalResponse
from dns_config.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dns_config.Configuration(
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
with dns_config.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dns_config.GlobalApi(api_client)
    body = dns_config.DNSGlobal() # DNSGlobal | 

    try:
        # Update the Global configuration object.
        api_response = api_instance.Update(body)
        print("The response of GlobalApi->Update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApi->Update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DNSGlobal**](DNSGlobal.md)|  | 

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

# **Update2**
> UpdateGlobalResponse Update2(id, body)

Update the Global configuration object.

Use this method to update the Global configuration object. Service operates on Global singleton object that represents parent configuration settings for inheritance.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dns_config
from dns_config.models.dns_global import DNSGlobal
from dns_config.models.update_global_response import UpdateGlobalResponse
from dns_config.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dns_config.Configuration(
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
with dns_config.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dns_config.GlobalApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = dns_config.DNSGlobal() # DNSGlobal | 

    try:
        # Update the Global configuration object.
        api_response = api_instance.Update2(id, body)
        print("The response of GlobalApi->Update2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApi->Update2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**DNSGlobal**](DNSGlobal.md)|  | 

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

