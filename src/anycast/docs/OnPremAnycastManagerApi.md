# anycast.OnPremAnycastManagerApi

All URIs are relative to *http://csp.infoblox.com/api/anycast/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateAnycastConfig**](OnPremAnycastManagerApi.md#CreateAnycastConfig) | **POST** /accm/ac_configs | Create Anycast Configuration
[**CreateAnycastVersion**](OnPremAnycastManagerApi.md#CreateAnycastVersion) | **POST** /accm/ac_version/{id} | Create Anycast Version
[**DeleteAnycastConfig**](OnPremAnycastManagerApi.md#DeleteAnycastConfig) | **DELETE** /accm/ac_configs/{id} | Delete Anycast Configuration
[**DeleteAnycastVersion**](OnPremAnycastManagerApi.md#DeleteAnycastVersion) | **DELETE** /accm/ac_version/{id} | Delete anycast version
[**DeleteOnpremHost**](OnPremAnycastManagerApi.md#DeleteOnpremHost) | **DELETE** /accm/op_hosts/{id} | Delete On-Prem Host
[**GetAnycastConfig**](OnPremAnycastManagerApi.md#GetAnycastConfig) | **GET** /accm/ac_configs/{id} | Retrieve Anycast Configuration
[**GetAnycastConfigList**](OnPremAnycastManagerApi.md#GetAnycastConfigList) | **GET** /accm/ac_configs | Retrieve Multiple Anycast Configurations
[**GetAnycastVersion**](OnPremAnycastManagerApi.md#GetAnycastVersion) | **GET** /accm/ac_version/{id} | Retrieve Anycast Version
[**GetOnpremConfig**](OnPremAnycastManagerApi.md#GetOnpremConfig) | **GET** /accm/oph_configs/{ophid}/{version} | Retrieve Generated, Per-Host Anycast Configuration
[**GetOnpremConfig2**](OnPremAnycastManagerApi.md#GetOnpremConfig2) | **GET** /onprem_config/{ophid}/{version} | Retrieve Generated, Per-Host Anycast Configuration
[**GetOnpremHost**](OnPremAnycastManagerApi.md#GetOnpremHost) | **GET** /accm/op_hosts/{id} | Retrieve On-Prem Host
[**GetStatus**](OnPremAnycastManagerApi.md#GetStatus) | **GET** /accm/oph_config_statuses/{ophid}/latest | Retrieve Configuration Status
[**GetStatus2**](OnPremAnycastManagerApi.md#GetStatus2) | **GET** /onprem_config_statuses/{ophid}/latest | Retrieve Configuration Status
[**ListAnycastConfigsWithRuntimeStatus**](OnPremAnycastManagerApi.md#ListAnycastConfigsWithRuntimeStatus) | **GET** /accm/ac_runtime_statuses | Read list of Anycast Configurations
[**ReadAnycastConfigWithRuntimeStatus**](OnPremAnycastManagerApi.md#ReadAnycastConfigWithRuntimeStatus) | **GET** /accm/ac_runtime_statuses/{id} | Read Anycast Configuration
[**UpdateAnycastConfig**](OnPremAnycastManagerApi.md#UpdateAnycastConfig) | **PUT** /accm/ac_configs/{id} | Create or Update Anycast Configuration
[**UpdateOnpremHost**](OnPremAnycastManagerApi.md#UpdateOnpremHost) | **PUT** /accm/op_hosts/{id} | Create or Update On-Prem Host


# **CreateAnycastConfig**
> AnycastConfigResponse CreateAnycastConfig(body)

Create Anycast Configuration

Use this method to create anycast configuration, as per the specified payload. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.models.anycast_config import AnycastConfig
from anycast.models.anycast_config_response import AnycastConfigResponse
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    body = anycast.AnycastConfig() # AnycastConfig | 

    try:
        # Create Anycast Configuration
        api_response = api_instance.CreateAnycastConfig(body)
        print("The response of OnPremAnycastManagerApi->CreateAnycastConfig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->CreateAnycastConfig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnycastConfig**](AnycastConfig.md)|  | 

### Return type

[**AnycastConfigResponse**](AnycastConfigResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | POST operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateAnycastVersion**
> object CreateAnycastVersion(id)

Create Anycast Version

Use this method to create anycast 2.0 version for the account ID @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Create Anycast Version
        api_response = api_instance.CreateAnycastVersion(id)
        print("The response of OnPremAnycastManagerApi->CreateAnycastVersion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->CreateAnycastVersion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | POST operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteAnycastConfig**
> object DeleteAnycastConfig(id)

Delete Anycast Configuration

Use this method to delete the addressed anycast configuration. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Delete Anycast Configuration
        api_response = api_instance.DeleteAnycastConfig(id)
        print("The response of OnPremAnycastManagerApi->DeleteAnycastConfig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->DeleteAnycastConfig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DELETE operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteAnycastVersion**
> object DeleteAnycastVersion(id)

Delete anycast version

Use this method to delete anycast 2.0 version associated with the given account id @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Delete anycast version
        api_response = api_instance.DeleteAnycastVersion(id)
        print("The response of OnPremAnycastManagerApi->DeleteAnycastVersion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->DeleteAnycastVersion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DELETE operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteOnpremHost**
> object DeleteOnpremHost(id)

Delete On-Prem Host

Use this method to delete the addressed on-prem host. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Delete On-Prem Host
        api_response = api_instance.DeleteOnpremHost(id)
        print("The response of OnPremAnycastManagerApi->DeleteOnpremHost:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->DeleteOnpremHost: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DELETE operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAnycastConfig**
> AnycastConfigResponse GetAnycastConfig(id)

Retrieve Anycast Configuration

Use this method to retrieve the specified anycast configuration, together with the list of member hosts. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.models.anycast_config_response import AnycastConfigResponse
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve Anycast Configuration
        api_response = api_instance.GetAnycastConfig(id)
        print("The response of OnPremAnycastManagerApi->GetAnycastConfig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->GetAnycastConfig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AnycastConfigResponse**](AnycastConfigResponse.md)

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

# **GetAnycastConfigList**
> GetAnycastConfigListResponse GetAnycastConfigList(account_id=account_id, service=service, host_id=host_id, ophid=ophid, is_configured=is_configured, tfilter=tfilter, torder_by=torder_by)

Retrieve Multiple Anycast Configurations

Without any filtering, use this method to retrieve all named anycast configurations for the account of authorization. Anycast configuration comprises common anycast configuration data that is defined in support of one service on a set of on-prem hosts. The anycast configurations resulting from this call will not include the list(s) of member hosts. Retrieving the list of member hosts requires the GET operation on single anycast configuration resource. If the account has no anycast configurations defined, the result of this call will be an empty list. @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.models.get_anycast_config_list_response import GetAnycastConfigListResponse
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    account_id = 56 # int |  (optional)
    service = 'service_example' # str |  (optional)
    host_id = 56 # int |  (optional)
    ophid = 'ophid_example' # str |  (optional)
    is_configured = True # bool |  (optional)
    tfilter = 'tfilter_example' # str |  (optional)
    torder_by = 'torder_by_example' # str |  (optional)

    try:
        # Retrieve Multiple Anycast Configurations
        api_response = api_instance.GetAnycastConfigList(account_id=account_id, service=service, host_id=host_id, ophid=ophid, is_configured=is_configured, tfilter=tfilter, torder_by=torder_by)
        print("The response of OnPremAnycastManagerApi->GetAnycastConfigList:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->GetAnycastConfigList: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | [optional] 
 **service** | **str**|  | [optional] 
 **host_id** | **int**|  | [optional] 
 **ophid** | **str**|  | [optional] 
 **is_configured** | **bool**|  | [optional] 
 **tfilter** | **str**|  | [optional] 
 **torder_by** | **str**|  | [optional] 

### Return type

[**GetAnycastConfigListResponse**](GetAnycastConfigListResponse.md)

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

# **GetAnycastVersion**
> AnycastVersion GetAnycastVersion(id)

Retrieve Anycast Version

Use this method to retrieve the anycast version for the given account id @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.models.anycast_version import AnycastVersion
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve Anycast Version
        api_response = api_instance.GetAnycastVersion(id)
        print("The response of OnPremAnycastManagerApi->GetAnycastVersion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->GetAnycastVersion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AnycastVersion**](AnycastVersion.md)

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

# **GetOnpremConfig**
> ServiceConfig GetOnpremConfig(ophid, version, app_name=app_name, app_version=app_version)

Retrieve Generated, Per-Host Anycast Configuration

Use this method to retrieve generated anycast configuration for anycast-enabled on-prem host. Retrieved configuration includes both interface and routing configuration. See common config manager documentation for the description of the returned payload. \"ophid\" is the system-assigned unique character-string identifier of the host. \"version\" can be either the timestamp of the configuration version that is sought after, or the word \"latest\". \"latest\" signifies the most recent generated configuration for this host. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.models.service_config import ServiceConfig
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    ophid = 'ophid_example' # str | 
    version = 'version_example' # str | 
    app_name = 'app_name_example' # str |  (optional)
    app_version = 'app_version_example' # str |  (optional)

    try:
        # Retrieve Generated, Per-Host Anycast Configuration
        api_response = api_instance.GetOnpremConfig(ophid, version, app_name=app_name, app_version=app_version)
        print("The response of OnPremAnycastManagerApi->GetOnpremConfig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->GetOnpremConfig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ophid** | **str**|  | 
 **version** | **str**|  | 
 **app_name** | **str**|  | [optional] 
 **app_version** | **str**|  | [optional] 

### Return type

[**ServiceConfig**](ServiceConfig.md)

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

# **GetOnpremConfig2**
> ServiceConfig GetOnpremConfig2(ophid, version, app_name=app_name, app_version=app_version)

Retrieve Generated, Per-Host Anycast Configuration

Use this method to retrieve generated anycast configuration for anycast-enabled on-prem host. Retrieved configuration includes both interface and routing configuration. See common config manager documentation for the description of the returned payload. \"ophid\" is the system-assigned unique character-string identifier of the host. \"version\" can be either the timestamp of the configuration version that is sought after, or the word \"latest\". \"latest\" signifies the most recent generated configuration for this host. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.models.service_config import ServiceConfig
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    ophid = 'ophid_example' # str | 
    version = 'version_example' # str | 
    app_name = 'app_name_example' # str |  (optional)
    app_version = 'app_version_example' # str |  (optional)

    try:
        # Retrieve Generated, Per-Host Anycast Configuration
        api_response = api_instance.GetOnpremConfig2(ophid, version, app_name=app_name, app_version=app_version)
        print("The response of OnPremAnycastManagerApi->GetOnpremConfig2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->GetOnpremConfig2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ophid** | **str**|  | 
 **version** | **str**|  | 
 **app_name** | **str**|  | [optional] 
 **app_version** | **str**|  | [optional] 

### Return type

[**ServiceConfig**](ServiceConfig.md)

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

# **GetOnpremHost**
> OnpremHostResponse GetOnpremHost(id)

Retrieve On-Prem Host

Use this method to retrieve the specified on-prem host from the anycast database. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.models.onprem_host_response import OnpremHostResponse
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve On-Prem Host
        api_response = api_instance.GetOnpremHost(id)
        print("The response of OnPremAnycastManagerApi->GetOnpremHost:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->GetOnpremHost: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OnpremHostResponse**](OnpremHostResponse.md)

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

# **GetStatus**
> ServiceStatusUpdateRequest GetStatus(ophid)

Retrieve Configuration Status

Use this method to retrieve configuration status for the specified host. The configuration status is retrieved from the anycast service database.  \"ophid\" is the system-assigned unique character-string identifier of the host. \"version\" parameter can be either the timestamp of the configuration version that is sought after, or the word \"latest\". \"latest' signifies the most recent generated configuration for this host. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.models.service_status_update_request import ServiceStatusUpdateRequest
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    ophid = 'ophid_example' # str | 

    try:
        # Retrieve Configuration Status
        api_response = api_instance.GetStatus(ophid)
        print("The response of OnPremAnycastManagerApi->GetStatus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->GetStatus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ophid** | **str**|  | 

### Return type

[**ServiceStatusUpdateRequest**](ServiceStatusUpdateRequest.md)

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

# **GetStatus2**
> ServiceStatusUpdateRequest GetStatus2(ophid)

Retrieve Configuration Status

Use this method to retrieve configuration status for the specified host. The configuration status is retrieved from the anycast service database.  \"ophid\" is the system-assigned unique character-string identifier of the host. \"version\" parameter can be either the timestamp of the configuration version that is sought after, or the word \"latest\". \"latest' signifies the most recent generated configuration for this host. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.models.service_status_update_request import ServiceStatusUpdateRequest
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    ophid = 'ophid_example' # str | 

    try:
        # Retrieve Configuration Status
        api_response = api_instance.GetStatus2(ophid)
        print("The response of OnPremAnycastManagerApi->GetStatus2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->GetStatus2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ophid** | **str**|  | 

### Return type

[**ServiceStatusUpdateRequest**](ServiceStatusUpdateRequest.md)

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

# **ListAnycastConfigsWithRuntimeStatus**
> GetAnycastConfigListResponse ListAnycastConfigsWithRuntimeStatus(account_id=account_id, service=service, host_id=host_id, ophid=ophid, is_configured=is_configured, tfilter=tfilter, torder_by=torder_by)

Read list of Anycast Configurations

Without any filtering, use this method to retrieve all named anycast configurations for the account of authorization. Anycast configuration comprises common anycast configuration data that is defined in support of one service on a set of on-prem hosts. The anycast configurations resulting from this call will not include the list(s) of member hosts. Retrieving the list of member hosts requires the GET operation on single anycast configuration resource. If the account has no anycast configurations defined, the result of this call will be an empty list. @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.models.get_anycast_config_list_response import GetAnycastConfigListResponse
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    account_id = 56 # int |  (optional)
    service = 'service_example' # str |  (optional)
    host_id = 56 # int |  (optional)
    ophid = 'ophid_example' # str |  (optional)
    is_configured = True # bool |  (optional)
    tfilter = 'tfilter_example' # str |  (optional)
    torder_by = 'torder_by_example' # str |  (optional)

    try:
        # Read list of Anycast Configurations
        api_response = api_instance.ListAnycastConfigsWithRuntimeStatus(account_id=account_id, service=service, host_id=host_id, ophid=ophid, is_configured=is_configured, tfilter=tfilter, torder_by=torder_by)
        print("The response of OnPremAnycastManagerApi->ListAnycastConfigsWithRuntimeStatus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->ListAnycastConfigsWithRuntimeStatus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | [optional] 
 **service** | **str**|  | [optional] 
 **host_id** | **int**|  | [optional] 
 **ophid** | **str**|  | [optional] 
 **is_configured** | **bool**|  | [optional] 
 **tfilter** | **str**|  | [optional] 
 **torder_by** | **str**|  | [optional] 

### Return type

[**GetAnycastConfigListResponse**](GetAnycastConfigListResponse.md)

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

# **ReadAnycastConfigWithRuntimeStatus**
> AnycastConfigResponse ReadAnycastConfigWithRuntimeStatus(id)

Read Anycast Configuration

Use this method to retrieve the specified anycast configuration, together with the list of member hosts. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.models.anycast_config_response import AnycastConfigResponse
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Read Anycast Configuration
        api_response = api_instance.ReadAnycastConfigWithRuntimeStatus(id)
        print("The response of OnPremAnycastManagerApi->ReadAnycastConfigWithRuntimeStatus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->ReadAnycastConfigWithRuntimeStatus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AnycastConfigResponse**](AnycastConfigResponse.md)

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

# **UpdateAnycastConfig**
> AnycastConfigResponse UpdateAnycastConfig(id, body)

Create or Update Anycast Configuration

Use this method to replace the addressed anycast configuration with configuration from the payload. If the addressed configuration does not exist, it will be created. Anycast configuration specified in the payload may contain the list of on-prem hosts that are supposed to be established as members of the specified configuration. If the anycast service has no information about one or more hosts from this list, such hosts will be created in the anycast service database. Note that the anycast service includes a background capability that verifies the validity of host data entered this way. This capability will delete any hosts created in this way that are determined to be invalid. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.models.anycast_config import AnycastConfig
from anycast.models.anycast_config_response import AnycastConfigResponse
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 
    body = anycast.AnycastConfig() # AnycastConfig | 

    try:
        # Create or Update Anycast Configuration
        api_response = api_instance.UpdateAnycastConfig(id, body)
        print("The response of OnPremAnycastManagerApi->UpdateAnycastConfig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->UpdateAnycastConfig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**AnycastConfig**](AnycastConfig.md)|  | 

### Return type

[**AnycastConfigResponse**](AnycastConfigResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PUT operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateOnpremHost**
> OnpremHostResponse UpdateOnpremHost(id, body)

Create or Update On-Prem Host

Use this method to create or update the addressed host as per the specified payload. The payload is supposed to provide complete replacement for the host data. If the addressed host does not exist, it will be created. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import anycast
from anycast.models.onprem_host import OnpremHost
from anycast.models.onprem_host_response import OnpremHostResponse
from anycast.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/anycast/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = anycast.Configuration(
    host = "http://csp.infoblox.com/api/anycast/v1"
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
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | Numeric host identifier
    body = anycast.OnpremHost() # OnpremHost | 

    try:
        # Create or Update On-Prem Host
        api_response = api_instance.UpdateOnpremHost(id, body)
        print("The response of OnPremAnycastManagerApi->UpdateOnpremHost:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremAnycastManagerApi->UpdateOnpremHost: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric host identifier | 
 **body** | [**OnpremHost**](OnpremHost.md)|  | 

### Return type

[**OnpremHostResponse**](OnpremHostResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PUT operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

