# anycast.OnPremAnycastManagerApi

All URIs are relative to *http://csp.infoblox.com/api/anycast/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_anycast_config**](OnPremAnycastManagerApi.md#create_anycast_config) | **POST** /accm/ac_configs | Create Anycast Configuration
[**create_anycast_version**](OnPremAnycastManagerApi.md#create_anycast_version) | **POST** /accm/ac_version/{id} | Create Anycast Version
[**delete_anycast_config**](OnPremAnycastManagerApi.md#delete_anycast_config) | **DELETE** /accm/ac_configs/{id} | Delete Anycast Configuration
[**delete_anycast_version**](OnPremAnycastManagerApi.md#delete_anycast_version) | **DELETE** /accm/ac_version/{id} | Delete anycast version
[**delete_onprem_host**](OnPremAnycastManagerApi.md#delete_onprem_host) | **DELETE** /accm/op_hosts/{id} | Delete On-Prem Host
[**get_anycast_config**](OnPremAnycastManagerApi.md#get_anycast_config) | **GET** /accm/ac_configs/{id} | Retrieve Anycast Configuration
[**get_anycast_config_list**](OnPremAnycastManagerApi.md#get_anycast_config_list) | **GET** /accm/ac_configs | Retrieve Multiple Anycast Configurations
[**get_anycast_version**](OnPremAnycastManagerApi.md#get_anycast_version) | **GET** /accm/ac_version/{id} | Retrieve Anycast Version
[**get_onprem_config**](OnPremAnycastManagerApi.md#get_onprem_config) | **GET** /accm/oph_configs/{ophid}/{version} | Retrieve Generated, Per-Host Anycast Configuration
[**get_onprem_config2**](OnPremAnycastManagerApi.md#get_onprem_config2) | **GET** /onprem_config/{ophid}/{version} | Retrieve Generated, Per-Host Anycast Configuration
[**get_onprem_host**](OnPremAnycastManagerApi.md#get_onprem_host) | **GET** /accm/op_hosts/{id} | Retrieve On-Prem Host
[**get_status**](OnPremAnycastManagerApi.md#get_status) | **GET** /accm/oph_config_statuses/{ophid}/latest | Retrieve Configuration Status
[**get_status2**](OnPremAnycastManagerApi.md#get_status2) | **GET** /onprem_config_statuses/{ophid}/latest | Retrieve Configuration Status
[**list_anycast_configs_with_runtime_status**](OnPremAnycastManagerApi.md#list_anycast_configs_with_runtime_status) | **GET** /accm/ac_runtime_statuses | Read list of Anycast Configurations
[**read_anycast_config_with_runtime_status**](OnPremAnycastManagerApi.md#read_anycast_config_with_runtime_status) | **GET** /accm/ac_runtime_statuses/{id} | Read Anycast Configuration
[**update_anycast_config**](OnPremAnycastManagerApi.md#update_anycast_config) | **PUT** /accm/ac_configs/{id} | Create or Update Anycast Configuration
[**update_onprem_host**](OnPremAnycastManagerApi.md#update_onprem_host) | **PUT** /accm/op_hosts/{id} | Create or Update On-Prem Host


# **create_anycast_config**
> AnycastConfigResponse create_anycast_config(body)

Create Anycast Configuration

Use this method to create anycast configuration, as per the specified payload. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    body = anycast.AnycastConfig() # AnycastConfig | 

    try:
        # Create Anycast Configuration
        api_response = api_instance.create_anycast_config(body)
        pprint("The response of OnPremAnycastManagerApi->create_anycast_config:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->create_anycast_config: %s\n" % e)
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

# **create_anycast_version**
> object create_anycast_version(id)

Create Anycast Version

Use this method to create anycast 2.0 version for the account ID @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Create Anycast Version
        api_response = api_instance.create_anycast_version(id)
        pprint("The response of OnPremAnycastManagerApi->create_anycast_version:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->create_anycast_version: %s\n" % e)
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

# **delete_anycast_config**
> object delete_anycast_config(id)

Delete Anycast Configuration

Use this method to delete the addressed anycast configuration. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Delete Anycast Configuration
        api_response = api_instance.delete_anycast_config(id)
        pprint("The response of OnPremAnycastManagerApi->delete_anycast_config:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->delete_anycast_config: %s\n" % e)
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

# **delete_anycast_version**
> object delete_anycast_version(id)

Delete anycast version

Use this method to delete anycast 2.0 version associated with the given account id @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Delete anycast version
        api_response = api_instance.delete_anycast_version(id)
        pprint("The response of OnPremAnycastManagerApi->delete_anycast_version:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->delete_anycast_version: %s\n" % e)
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

# **delete_onprem_host**
> object delete_onprem_host(id)

Delete On-Prem Host

Use this method to delete the addressed on-prem host. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Delete On-Prem Host
        api_response = api_instance.delete_onprem_host(id)
        pprint("The response of OnPremAnycastManagerApi->delete_onprem_host:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->delete_onprem_host: %s\n" % e)
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

# **get_anycast_config**
> AnycastConfigResponse get_anycast_config(id)

Retrieve Anycast Configuration

Use this method to retrieve the specified anycast configuration, together with the list of member hosts. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve Anycast Configuration
        api_response = api_instance.get_anycast_config(id)
        pprint("The response of OnPremAnycastManagerApi->get_anycast_config:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->get_anycast_config: %s\n" % e)
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

# **get_anycast_config_list**
> GetAnycastConfigListResponse get_anycast_config_list(account_id=account_id, service=service, host_id=host_id, ophid=ophid, is_configured=is_configured, tfilter=tfilter, torder_by=torder_by)

Retrieve Multiple Anycast Configurations

Without any filtering, use this method to retrieve all named anycast configurations for the account of authorization. Anycast configuration comprises common anycast configuration data that is defined in support of one service on a set of on-prem hosts. The anycast configurations resulting from this call will not include the list(s) of member hosts. Retrieving the list of member hosts requires the GET operation on single anycast configuration resource. If the account has no anycast configurations defined, the result of this call will be an empty list. @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)

    try:
        # Retrieve Multiple Anycast Configurations
        api_response = api_instance.get_anycast_config_list()
        pprint("The response of OnPremAnycastManagerApi->get_anycast_config_list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->get_anycast_config_list: %s\n" % e)
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

# **get_anycast_version**
> AnycastVersion get_anycast_version(id)

Retrieve Anycast Version

Use this method to retrieve the anycast version for the given account id @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve Anycast Version
        api_response = api_instance.get_anycast_version(id)
        pprint("The response of OnPremAnycastManagerApi->get_anycast_version:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->get_anycast_version: %s\n" % e)
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

# **get_onprem_config**
> ServiceConfig get_onprem_config(ophid, version, app_name=app_name, app_version=app_version)

Retrieve Generated, Per-Host Anycast Configuration

Use this method to retrieve generated anycast configuration for anycast-enabled on-prem host. Retrieved configuration includes both interface and routing configuration. See common config manager documentation for the description of the returned payload. \"ophid\" is the system-assigned unique character-string identifier of the host. \"version\" can be either the timestamp of the configuration version that is sought after, or the word \"latest\". \"latest\" signifies the most recent generated configuration for this host. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    ophid = 'ophid_example' # str | 
    version = 'version_example' # str | 

    try:
        # Retrieve Generated, Per-Host Anycast Configuration
        api_response = api_instance.get_onprem_config(ophid, version)
        pprint("The response of OnPremAnycastManagerApi->get_onprem_config:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->get_onprem_config: %s\n" % e)
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

# **get_onprem_config2**
> ServiceConfig get_onprem_config2(ophid, version, app_name=app_name, app_version=app_version)

Retrieve Generated, Per-Host Anycast Configuration

Use this method to retrieve generated anycast configuration for anycast-enabled on-prem host. Retrieved configuration includes both interface and routing configuration. See common config manager documentation for the description of the returned payload. \"ophid\" is the system-assigned unique character-string identifier of the host. \"version\" can be either the timestamp of the configuration version that is sought after, or the word \"latest\". \"latest\" signifies the most recent generated configuration for this host. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    ophid = 'ophid_example' # str | 
    version = 'version_example' # str | 

    try:
        # Retrieve Generated, Per-Host Anycast Configuration
        api_response = api_instance.get_onprem_config2(ophid, version)
        pprint("The response of OnPremAnycastManagerApi->get_onprem_config2:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->get_onprem_config2: %s\n" % e)
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

# **get_onprem_host**
> OnpremHostResponse get_onprem_host(id)

Retrieve On-Prem Host

Use this method to retrieve the specified on-prem host from the anycast database. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve On-Prem Host
        api_response = api_instance.get_onprem_host(id)
        pprint("The response of OnPremAnycastManagerApi->get_onprem_host:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->get_onprem_host: %s\n" % e)
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

# **get_status**
> ServiceStatusUpdateRequest get_status(ophid)

Retrieve Configuration Status

Use this method to retrieve configuration status for the specified host. The configuration status is retrieved from the anycast service database.  \"ophid\" is the system-assigned unique character-string identifier of the host. \"version\" parameter can be either the timestamp of the configuration version that is sought after, or the word \"latest\". \"latest' signifies the most recent generated configuration for this host. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    ophid = 'ophid_example' # str | 

    try:
        # Retrieve Configuration Status
        api_response = api_instance.get_status(ophid)
        pprint("The response of OnPremAnycastManagerApi->get_status:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->get_status: %s\n" % e)
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

# **get_status2**
> ServiceStatusUpdateRequest get_status2(ophid)

Retrieve Configuration Status

Use this method to retrieve configuration status for the specified host. The configuration status is retrieved from the anycast service database.  \"ophid\" is the system-assigned unique character-string identifier of the host. \"version\" parameter can be either the timestamp of the configuration version that is sought after, or the word \"latest\". \"latest' signifies the most recent generated configuration for this host. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    ophid = 'ophid_example' # str | 

    try:
        # Retrieve Configuration Status
        api_response = api_instance.get_status2(ophid)
        pprint("The response of OnPremAnycastManagerApi->get_status2:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->get_status2: %s\n" % e)
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

# **list_anycast_configs_with_runtime_status**
> GetAnycastConfigListResponse list_anycast_configs_with_runtime_status(account_id=account_id, service=service, host_id=host_id, ophid=ophid, is_configured=is_configured, tfilter=tfilter, torder_by=torder_by)

Read list of Anycast Configurations

Without any filtering, use this method to retrieve all named anycast configurations for the account of authorization. Anycast configuration comprises common anycast configuration data that is defined in support of one service on a set of on-prem hosts. The anycast configurations resulting from this call will not include the list(s) of member hosts. Retrieving the list of member hosts requires the GET operation on single anycast configuration resource. If the account has no anycast configurations defined, the result of this call will be an empty list. @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)

    try:
        # Read list of Anycast Configurations
        api_response = api_instance.list_anycast_configs_with_runtime_status()
        pprint("The response of OnPremAnycastManagerApi->list_anycast_configs_with_runtime_status:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->list_anycast_configs_with_runtime_status: %s\n" % e)
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

# **read_anycast_config_with_runtime_status**
> AnycastConfigResponse read_anycast_config_with_runtime_status(id)

Read Anycast Configuration

Use this method to retrieve the specified anycast configuration, together with the list of member hosts. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.404._error {\"code\": \"NOT_FOUND\", \"message\": \"\", \"status\": 404} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 

    try:
        # Read Anycast Configuration
        api_response = api_instance.read_anycast_config_with_runtime_status(id)
        pprint("The response of OnPremAnycastManagerApi->read_anycast_config_with_runtime_status:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->read_anycast_config_with_runtime_status: %s\n" % e)
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

# **update_anycast_config**
> AnycastConfigResponse update_anycast_config(id, body)

Create or Update Anycast Configuration

Use this method to replace the addressed anycast configuration with configuration from the payload. If the addressed configuration does not exist, it will be created. Anycast configuration specified in the payload may contain the list of on-prem hosts that are supposed to be established as members of the specified configuration. If the anycast service has no information about one or more hosts from this list, such hosts will be created in the anycast service database. Note that the anycast service includes a background capability that verifies the validity of host data entered this way. This capability will delete any hosts created in this way that are determined to be invalid. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | 
    body = anycast.AnycastConfig() # AnycastConfig | 

    try:
        # Create or Update Anycast Configuration
        api_response = api_instance.update_anycast_config(id, body)
        pprint("The response of OnPremAnycastManagerApi->update_anycast_config:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->update_anycast_config: %s\n" % e)
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

# **update_onprem_host**
> OnpremHostResponse update_onprem_host(id, body)

Create or Update On-Prem Host

Use this method to create or update the addressed host as per the specified payload. The payload is supposed to provide complete replacement for the host data. If the addressed host does not exist, it will be created. @responses.400._error {\"code\": \"INVALID_ARGUMENT\", \"message\": \"\", \"status\": 400} @responses.500._error {\"code\": \"INTERNAL\", \"message\": \"Internal Server Error\", \"status\": 500}

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import anycast

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    id = 56 # int | Numeric host identifier
    body = anycast.OnpremHost() # OnpremHost | 

    try:
        # Create or Update On-Prem Host
        api_response = api_instance.update_onprem_host(id, body)
        pprint("The response of OnPremAnycastManagerApi->update_onprem_host:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling OnPremAnycastManagerApi->update_onprem_host: %s\n" % e)
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

