# upgrade_policy.UpgradePolicyV2Api

All URIs are relative to *http://csp.infoblox.com/api/upgrade_policy*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_config_now**](UpgradePolicyV2Api.md#apply_config_now) | **POST** /v2/config/apply_now | Immediately apply the config updates object to the list of hosts
[**batch**](UpgradePolicyV2Api.md#batch) | **POST** /v2/maintenance_windows/batch | Create, update and/or delete multiple maintenance windows in a single request
[**create**](UpgradePolicyV2Api.md#create) | **POST** /v2/maintenance_windows | Create a maintenance window
[**delete**](UpgradePolicyV2Api.md#delete) | **DELETE** /v2/maintenance_windows/{id} | Delete maintenance window
[**get**](UpgradePolicyV2Api.md#get) | **GET** /v2/maintenance_windows/{id} | Read a maintenance window
[**list**](UpgradePolicyV2Api.md#list) | **GET** /v2/maintenance_windows | List all the maintenance windows
[**update**](UpgradePolicyV2Api.md#update) | **PATCH** /v2/maintenance_windows/{id} | Update an existing maintenance window


# **apply_config_now**
> ApplyConfigNowResponse apply_config_now(body)

Immediately apply the config updates object to the list of hosts

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import upgrade_policy

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upgrade_policy.UpgradePolicyV2Api(api_client)
    body = upgrade_policy.ApplyConfigNowRequest() # ApplyConfigNowRequest | 

    try:
        # Immediately apply the config updates object to the list of hosts
        api_response = api_instance.apply_config_now(body)
        pprint("The response of UpgradePolicyV2Api->apply_config_now:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UpgradePolicyV2Api->apply_config_now: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyConfigNowRequest**](ApplyConfigNowRequest.md)|  | 

### Return type

[**ApplyConfigNowResponse**](ApplyConfigNowResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch**
> BatchMaintenanceWindowResponse batch(body)

Create, update and/or delete multiple maintenance windows in a single request

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import upgrade_policy

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upgrade_policy.UpgradePolicyV2Api(api_client)
    body = upgrade_policy.BatchMaintenanceWindowRequest() # BatchMaintenanceWindowRequest | 

    try:
        # Create, update and/or delete multiple maintenance windows in a single request
        api_response = api_instance.batch(body)
        pprint("The response of UpgradePolicyV2Api->batch:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UpgradePolicyV2Api->batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchMaintenanceWindowRequest**](BatchMaintenanceWindowRequest.md)|  | 

### Return type

[**BatchMaintenanceWindowResponse**](BatchMaintenanceWindowResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> CreateMaintenanceWindowResponse create(body)

Create a maintenance window

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import upgrade_policy

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upgrade_policy.UpgradePolicyV2Api(api_client)
    body = upgrade_policy.CreateMaintenanceWindowRequest() # CreateMaintenanceWindowRequest | 

    try:
        # Create a maintenance window
        api_response = api_instance.create(body)
        pprint("The response of UpgradePolicyV2Api->create:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UpgradePolicyV2Api->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMaintenanceWindowRequest**](CreateMaintenanceWindowRequest.md)|  | 

### Return type

[**CreateMaintenanceWindowResponse**](CreateMaintenanceWindowResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> DeleteMaintenanceWindowResponse delete(id)

Delete maintenance window

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import upgrade_policy

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upgrade_policy.UpgradePolicyV2Api(api_client)
    id = 'id_example' # str | uuid of a maintenance window record

    try:
        # Delete maintenance window
        api_response = api_instance.delete(id)
        pprint("The response of UpgradePolicyV2Api->delete:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UpgradePolicyV2Api->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| uuid of a maintenance window record | 

### Return type

[**DeleteMaintenanceWindowResponse**](DeleteMaintenanceWindowResponse.md)

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

# **get**
> GetMaintenanceWindowResponse get(id)

Read a maintenance window

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import upgrade_policy

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upgrade_policy.UpgradePolicyV2Api(api_client)
    id = 'id_example' # str | uuid of a maintenance window record

    try:
        # Read a maintenance window
        api_response = api_instance.get(id)
        pprint("The response of UpgradePolicyV2Api->get:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UpgradePolicyV2Api->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| uuid of a maintenance window record | 

### Return type

[**GetMaintenanceWindowResponse**](GetMaintenanceWindowResponse.md)

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

# **list**
> ListMaintenanceWindowResponse list(window_type=window_type)

List all the maintenance windows

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import upgrade_policy

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upgrade_policy.UpgradePolicyV2Api(api_client)

    try:
        # List all the maintenance windows
        api_response = api_instance.list()
        pprint("The response of UpgradePolicyV2Api->list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UpgradePolicyV2Api->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **window_type** | **str**| window type (software or config). | [optional] 

### Return type

[**ListMaintenanceWindowResponse**](ListMaintenanceWindowResponse.md)

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
> UpdateMaintenanceWindowResponse update(id, body)

Update an existing maintenance window

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import upgrade_policy

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upgrade_policy.UpgradePolicyV2Api(api_client)
    id = 'id_example' # str | uuid of a maintenance window record
    body = upgrade_policy.UpdateMaintenanceWindowRequest() # UpdateMaintenanceWindowRequest | 

    try:
        # Update an existing maintenance window
        api_response = api_instance.update(id, body)
        pprint("The response of UpgradePolicyV2Api->update:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UpgradePolicyV2Api->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| uuid of a maintenance window record | 
 **body** | [**UpdateMaintenanceWindowRequest**](UpdateMaintenanceWindowRequest.md)|  | 

### Return type

[**UpdateMaintenanceWindowResponse**](UpdateMaintenanceWindowResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PATCH operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

