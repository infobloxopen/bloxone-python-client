# ipam.AddressBlockApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy**](AddressBlockApi.md#copy) | **POST** /ipam/address_block/{id}/copy | Copy the address block.
[**create**](AddressBlockApi.md#create) | **POST** /ipam/address_block | Create the address block.
[**create_next_available_ab**](AddressBlockApi.md#create_next_available_ab) | **POST** /ipam/address_block/{id}/nextavailableaddressblock | Create the Next Available Address Block object.
[**create_next_available_ip**](AddressBlockApi.md#create_next_available_ip) | **POST** /ipam/address_block/{id}/nextavailableip | Allocate the next available IP address.
[**create_next_available_subnet**](AddressBlockApi.md#create_next_available_subnet) | **POST** /ipam/address_block/{id}/nextavailablesubnet | Create the Next Available Subnet object.
[**delete**](AddressBlockApi.md#delete) | **DELETE** /ipam/address_block/{id} | Move the address block to the recycle bin.
[**list**](AddressBlockApi.md#list) | **GET** /ipam/address_block | Retrieve the address blocks.
[**list_ancestor**](AddressBlockApi.md#list_ancestor) | **GET** /ipam/address_block/{id}/ancestor | Retrieve address block ancestors.
[**list_next_available_ab**](AddressBlockApi.md#list_next_available_ab) | **GET** /ipam/address_block/{id}/nextavailableaddressblock | List Next Available Address Block objects.
[**list_next_available_ip**](AddressBlockApi.md#list_next_available_ip) | **GET** /ipam/address_block/{id}/nextavailableip | Retrieve the next available IP address.
[**list_next_available_subnet**](AddressBlockApi.md#list_next_available_subnet) | **GET** /ipam/address_block/{id}/nextavailablesubnet | List Next Available Subnet objects.
[**read**](AddressBlockApi.md#read) | **GET** /ipam/address_block/{id} | Retrieve the address block.
[**update**](AddressBlockApi.md#update) | **PATCH** /ipam/address_block/{id} | Update the address block.


# **copy**
> CopyAddressBlockResponse copy(id, body)

Copy the address block.

Use this method to copy an __AddressBlock__ object. The __AddressBlock__ object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = ipam.CopyAddressBlock() # CopyAddressBlock | 

    try:
        # Copy the address block.
        api_response = api_instance.copy(id, body)
        pprint("The response of AddressBlockApi->copy:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AddressBlockApi->copy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**CopyAddressBlock**](CopyAddressBlock.md)|  | 

### Return type

[**CopyAddressBlockResponse**](CopyAddressBlockResponse.md)

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

# **create**
> CreateAddressBlockResponse create(body, inherit=inherit)

Create the address block.

Use this method to create an __AddressBlock__ object. The __AddressBlock__ object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

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
    api_instance = ipam.AddressBlockApi(api_client)
    body = ipam.AddressBlock() # AddressBlock | 

    try:
        # Create the address block.
        api_response = api_instance.create(body)
        pprint("The response of AddressBlockApi->create:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AddressBlockApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddressBlock**](AddressBlock.md)|  | 
 **inherit** | **str**| This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none | [optional] 

### Return type

[**CreateAddressBlockResponse**](CreateAddressBlockResponse.md)

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

# **create_next_available_ab**
> CreateNextAvailableABResponse create_next_available_ab(id, cidr, count=count, name=name, comment=comment)

Create the Next Available Address Block object.

Use this method to create a Next Available __AddressBlock__ object. The Next Available Address Block is a generator that allocates one or more _ipam/address_block_ resource from available address blocks when the network address is not known prior to allocation.

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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    cidr = 56 # int | The cidr value of address blocks to be created.

    try:
        # Create the Next Available Address Block object.
        api_response = api_instance.create_next_available_ab(id, cidr)
        pprint("The response of AddressBlockApi->create_next_available_ab:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AddressBlockApi->create_next_available_ab: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **cidr** | **int**| The cidr value of address blocks to be created. | 
 **count** | **int**| Number of address blocks to generate. Default 1 if not set. | [optional] [default to 1]
 **name** | **str**| Name of next available address blocks. | [optional] 
 **comment** | **str**| Comment of next available address blocks. | [optional] 

### Return type

[**CreateNextAvailableABResponse**](CreateNextAvailableABResponse.md)

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

# **create_next_available_ip**
> CreateNextAvailableIPResponse create_next_available_ip(id, contiguous=contiguous, count=count)

Allocate the next available IP address.

Use this method to allocate the next available IP address. This allocates one or more __Address__ (_ipam/address_) resource from available addresses, when the IP address is not known prior to allocation.

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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Allocate the next available IP address.
        api_response = api_instance.create_next_available_ip(id)
        pprint("The response of AddressBlockApi->create_next_available_ip:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AddressBlockApi->create_next_available_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **contiguous** | **bool**| Indicates whether the IP addresses should belong to a contiguous block.  Defaults to _false_. | [optional] [default to False]
 **count** | **int**| The number of IP addresses requested.  Defaults to 1. | [optional] [default to 1]

### Return type

[**CreateNextAvailableIPResponse**](CreateNextAvailableIPResponse.md)

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

# **create_next_available_subnet**
> CreateNextAvailableSubnetResponse create_next_available_subnet(id, cidr, count=count, name=name, comment=comment, dhcp_host=dhcp_host)

Create the Next Available Subnet object.

Use this method to create a Next Available __Subnet__ object. The Next Available Subnet is a generator that allocates one or more _ipam/subnet_ resource from available subnets when the network address is not known prior to allocation.

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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    cidr = 56 # int | The cidr value of subnets to be created.

    try:
        # Create the Next Available Subnet object.
        api_response = api_instance.create_next_available_subnet(id, cidr)
        pprint("The response of AddressBlockApi->create_next_available_subnet:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AddressBlockApi->create_next_available_subnet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **cidr** | **int**| The cidr value of subnets to be created. | 
 **count** | **int**| Number of subnets to generate. Default 1 if not set. | [optional] [default to 1]
 **name** | **str**| Name of next available subnets. | [optional] 
 **comment** | **str**| Comment of next available subnets. | [optional] 
 **dhcp_host** | **str**| Reference of OnPrem Host associated with the next available subnets to be created. | [optional] 

### Return type

[**CreateNextAvailableSubnetResponse**](CreateNextAvailableSubnetResponse.md)

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

# **delete**
> delete(id)

Move the address block to the recycle bin.

Use this method to move an __AddressBlock__ object to the recycle bin. The __AddressBlock__ object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Move the address block to the recycle bin.
        api_instance.delete(id)
    except Exception as e:
        pprint("Exception when calling AddressBlockApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListAddressBlockResponse list(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, torder_by=torder_by, tfilter=tfilter, inherit=inherit)

Retrieve the address blocks.

Use this method to retrieve __AddressBlock__ objects. The __AddressBlock__ object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

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
    api_instance = ipam.AddressBlockApi(api_client)

    try:
        # Retrieve the address blocks.
        api_response = api_instance.list()
        pprint("The response of AddressBlockApi->list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AddressBlockApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **torder_by** | **str**| This parameter is used for sorting by tags. | [optional] 
 **tfilter** | **str**| This parameter is used for filtering by tags. | [optional] 
 **inherit** | **str**| This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none | [optional] 

### Return type

[**ListAddressBlockResponse**](ListAddressBlockResponse.md)

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

# **list_ancestor**
> ListAncestorResponse list_ancestor(id)

Retrieve address block ancestors.

Use this method to retrieve the ancestors of the __AddressBlock__ object. This returns all the ancestors of the address block.

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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Retrieve address block ancestors.
        api_response = api_instance.list_ancestor(id)
        pprint("The response of AddressBlockApi->list_ancestor:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AddressBlockApi->list_ancestor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 

### Return type

[**ListAncestorResponse**](ListAncestorResponse.md)

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

# **list_next_available_ab**
> NextAvailableABResponse list_next_available_ab(id, cidr=cidr, count=count, name=name, comment=comment, federated_realms=federated_realms, compartment_id=compartment_id)

List Next Available Address Block objects.

Use this method to list Next Available __AddressBlock__ objects. The Next Available __AddressBlock__ is a generator that returns one or more _ipam/address_block_ resource from available address blocks when the network address is not known prior to allocation.

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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # List Next Available Address Block objects.
        api_response = api_instance.list_next_available_ab(id)
        pprint("The response of AddressBlockApi->list_next_available_ab:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AddressBlockApi->list_next_available_ab: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **cidr** | **int**| The cidr value of address blocks to be created. | [optional] 
 **count** | **int**| Number of address blocks to generate. Default 1 if not set. | [optional] 
 **name** | **str**| Name of next available address blocks. | [optional] 
 **comment** | **str**| Comment of next available address blocks. | [optional] 
 **federated_realms** | [**List[str]**](str.md)| Reserved for future use. | [optional] 
 **compartment_id** | **str**| The compartment id of the address blocks to be created. | [optional] 

### Return type

[**NextAvailableABResponse**](NextAvailableABResponse.md)

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

# **list_next_available_ip**
> NextAvailableIPResponse list_next_available_ip(id, contiguous=contiguous, count=count)

Retrieve the next available IP address.

Use this method to retrieve the next available IP address. This returns one or more __Address__ (_ipam/address_) resource from available addresses, when IP address is not known prior to allocation.

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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Retrieve the next available IP address.
        api_response = api_instance.list_next_available_ip(id)
        pprint("The response of AddressBlockApi->list_next_available_ip:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AddressBlockApi->list_next_available_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **contiguous** | **bool**| Indicates whether the IP addresses should belong to a contiguous block.  Defaults to _false_. | [optional] 
 **count** | **int**| The number of IP addresses requested.  Defaults to 1. | [optional] 

### Return type

[**NextAvailableIPResponse**](NextAvailableIPResponse.md)

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

# **list_next_available_subnet**
> NextAvailableSubnetResponse list_next_available_subnet(id, cidr=cidr, count=count, name=name, comment=comment, dhcp_host=dhcp_host, federated_realms=federated_realms)

List Next Available Subnet objects.

Use this method to list Next Available __Subnet__ objects. The Next Available Address Block is a generator that returns one or more _ipam/subnet_ resource from available subnets when the network address is not known prior to allocation.

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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # List Next Available Subnet objects.
        api_response = api_instance.list_next_available_subnet(id)
        pprint("The response of AddressBlockApi->list_next_available_subnet:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AddressBlockApi->list_next_available_subnet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **cidr** | **int**| The cidr value of subnets to be created. | [optional] 
 **count** | **int**| Number of subnets to generate. Default 1 if not set. | [optional] 
 **name** | **str**| Name of next available subnets. | [optional] 
 **comment** | **str**| Comment of next available subnets. | [optional] 
 **dhcp_host** | **str**| Reference of OnPrem Host associated with the next available subnets to be created. | [optional] 
 **federated_realms** | [**List[str]**](str.md)| Reserved for future use. | [optional] 

### Return type

[**NextAvailableSubnetResponse**](NextAvailableSubnetResponse.md)

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

# **read**
> ReadAddressBlockResponse read(id, fields=fields, inherit=inherit)

Retrieve the address block.

Use this method to retrieve an __AddressBlock__ object. The __AddressBlock__ object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Retrieve the address block.
        api_response = api_instance.read(id)
        pprint("The response of AddressBlockApi->read:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AddressBlockApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **inherit** | **str**| This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none | [optional] 

### Return type

[**ReadAddressBlockResponse**](ReadAddressBlockResponse.md)

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
> UpdateAddressBlockResponse update(id, body, inherit=inherit)

Update the address block.

Use this method to update an __AddressBlock__ object. The __AddressBlock__ object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = ipam.AddressBlock() # AddressBlock | 

    try:
        # Update the address block.
        api_response = api_instance.update(id, body)
        pprint("The response of AddressBlockApi->update:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AddressBlockApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**AddressBlock**](AddressBlock.md)|  | 
 **inherit** | **str**| This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none | [optional] 

### Return type

[**UpdateAddressBlockResponse**](UpdateAddressBlockResponse.md)

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

