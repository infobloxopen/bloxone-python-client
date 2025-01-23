# ipam.ConfigProfileApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associate_config_profile_to_objects**](ConfigProfileApi.md#associate_config_profile_to_objects) | **POST** /dhcp/config_profile/link_profile | Associate a config profile to objects.
[**associate_object_to_config_profiles**](ConfigProfileApi.md#associate_object_to_config_profiles) | **POST** /dhcp/config_profile/link_object | Associate an object to config profiles.
[**disassociate_config_profile_from_objects**](ConfigProfileApi.md#disassociate_config_profile_from_objects) | **POST** /dhcp/config_profile/delink_profile | Disassociate a config profile from objects.
[**disassociate_object_from_config_profiles**](ConfigProfileApi.md#disassociate_object_from_config_profiles) | **POST** /dhcp/config_profile/delink_object | Disassociate an object from a config profile.
[**list_config_profiles**](ConfigProfileApi.md#list_config_profiles) | **GET** /dhcp/config_profile/profiles | Retrieve config profiles.
[**list_subnets**](ConfigProfileApi.md#list_subnets) | **GET** /dhcp/config_profile/subnets | Retrieve subnets associated with a config profile.


# **associate_config_profile_to_objects**
> object associate_config_profile_to_objects(body)

Associate a config profile to objects.

Use this method to associate a __ConfigProfile__ with an object.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("UNIVERSAL_DDI_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = ipam.ConfigProfileApi(api_client)
    body = ipam.AssociateConfigProfileToObjectsRequest() # AssociateConfigProfileToObjectsRequest | 

    try:
        # Associate a config profile to objects.
        api_response = api_instance.associate_config_profile_to_objects(body)
        pprint("The response of ConfigProfileApi->associate_config_profile_to_objects:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling ConfigProfileApi->associate_config_profile_to_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssociateConfigProfileToObjectsRequest**](AssociateConfigProfileToObjectsRequest.md)|  | 

### Return type

**object**

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

# **associate_object_to_config_profiles**
> object associate_object_to_config_profiles(body)

Associate an object to config profiles.

Use this method to associate an object with a __ConfigProfile__.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("UNIVERSAL_DDI_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = ipam.ConfigProfileApi(api_client)
    body = ipam.AssociateObjectToConfigProfilesRequest() # AssociateObjectToConfigProfilesRequest | 

    try:
        # Associate an object to config profiles.
        api_response = api_instance.associate_object_to_config_profiles(body)
        pprint("The response of ConfigProfileApi->associate_object_to_config_profiles:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling ConfigProfileApi->associate_object_to_config_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssociateObjectToConfigProfilesRequest**](AssociateObjectToConfigProfilesRequest.md)|  | 

### Return type

**object**

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

# **disassociate_config_profile_from_objects**
> object disassociate_config_profile_from_objects(body)

Disassociate a config profile from objects.

Use this method to disassociate a __ConfigProfile__ from an object.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("UNIVERSAL_DDI_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = ipam.ConfigProfileApi(api_client)
    body = ipam.DisassociateConfigProfileFromObjectsRequest() # DisassociateConfigProfileFromObjectsRequest | 

    try:
        # Disassociate a config profile from objects.
        api_response = api_instance.disassociate_config_profile_from_objects(body)
        pprint("The response of ConfigProfileApi->disassociate_config_profile_from_objects:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling ConfigProfileApi->disassociate_config_profile_from_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DisassociateConfigProfileFromObjectsRequest**](DisassociateConfigProfileFromObjectsRequest.md)|  | 

### Return type

**object**

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

# **disassociate_object_from_config_profiles**
> object disassociate_object_from_config_profiles(body)

Disassociate an object from a config profile.

Use this method to disassociate an object from a __ConfigProfile__.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("UNIVERSAL_DDI_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = ipam.ConfigProfileApi(api_client)
    body = ipam.DisassociateObjectFromConfigProfilesRequest() # DisassociateObjectFromConfigProfilesRequest | 

    try:
        # Disassociate an object from a config profile.
        api_response = api_instance.disassociate_object_from_config_profiles(body)
        pprint("The response of ConfigProfileApi->disassociate_object_from_config_profiles:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling ConfigProfileApi->disassociate_object_from_config_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DisassociateObjectFromConfigProfilesRequest**](DisassociateObjectFromConfigProfilesRequest.md)|  | 

### Return type

**object**

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

# **list_config_profiles**
> ListConfigProfileResponse list_config_profiles(object_id=object_id)

Retrieve config profiles.

Use this method to retrieve __ConfigProfile__ objects.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("UNIVERSAL_DDI_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = ipam.ConfigProfileApi(api_client)

    try:
        # Retrieve config profiles.
        api_response = api_instance.list_config_profiles()
        pprint("The response of ConfigProfileApi->list_config_profiles:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling ConfigProfileApi->list_config_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**|  | [optional] 

### Return type

[**ListConfigProfileResponse**](ListConfigProfileResponse.md)

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

# **list_subnets**
> ListCPSubnetResponse list_subnets(config_profile_id=config_profile_id, order_by=order_by, offset=offset, limit=limit, page_token=page_token)

Retrieve subnets associated with a config profile.

Use this method to retrieve __Subnet__ objects associated with a __ConfigProfile__.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("UNIVERSAL_DDI_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = ipam.ConfigProfileApi(api_client)

    try:
        # Retrieve subnets associated with a config profile.
        api_response = api_instance.list_subnets()
        pprint("The response of ConfigProfileApi->list_subnets:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling ConfigProfileApi->list_subnets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_profile_id** | **str**|  | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 

### Return type

[**ListCPSubnetResponse**](ListCPSubnetResponse.md)

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

