# ipam.RangeApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](RangeApi.md#create) | **POST** /ipam/range | Create the range.
[**create_next_available_ip**](RangeApi.md#create_next_available_ip) | **POST** /ipam/range/{id}/nextavailableip | Allocate the next available IP address.
[**delete**](RangeApi.md#delete) | **DELETE** /ipam/range/{id} | Move the range to the recycle bin.
[**list**](RangeApi.md#list) | **GET** /ipam/range | Retrieve ranges.
[**list_next_available_ip**](RangeApi.md#list_next_available_ip) | **GET** /ipam/range/{id}/nextavailableip | Retrieve the next available IP address.
[**read**](RangeApi.md#read) | **GET** /ipam/range/{id} | Retrieve the range.
[**update**](RangeApi.md#update) | **PATCH** /ipam/range/{id} | Update the range.


# **create**
> CreateRangeResponse create(body, inherit=inherit)

Create the range.

Use this method to create a __Range__ object. A __Range__ object represents a set of contiguous IP addresses in the same IP space with no gap, expressed as a (start, end) pair within a given subnet that are grouped together for administrative purpose and protocol management. The start and end values are not required to align with CIDR boundaries.

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
    api_instance = ipam.RangeApi(api_client)
    body = ipam.Range() # Range | 

    try:
        # Create the range.
        api_response = api_instance.create(body)
        pprint("The response of RangeApi->create:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling RangeApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Range**](Range.md)|  | 
 **inherit** | **str**| This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none | [optional] 

### Return type

[**CreateRangeResponse**](CreateRangeResponse.md)

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
    api_instance = ipam.RangeApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Allocate the next available IP address.
        api_response = api_instance.create_next_available_ip(id)
        pprint("The response of RangeApi->create_next_available_ip:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling RangeApi->create_next_available_ip: %s\n" % e)
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

# **delete**
> delete(id)

Move the range to the recycle bin.

Use this method to move a __Range__ object to the recycle bin. A __Range__ object represents a set of contiguous IP addresses in the same IP space with no gap, expressed as a (start, end) pair within a given subnet that are grouped together for administrative purpose and protocol management. The start and end values are not required to align with CIDR boundaries.

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
    api_instance = ipam.RangeApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Move the range to the recycle bin.
        api_instance.delete(id)
    except Exception as e:
        pprint("Exception when calling RangeApi->delete: %s\n" % e)
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
> ListRangeResponse list(filter=filter, order_by=order_by, fields=fields, offset=offset, limit=limit, page_token=page_token, torder_by=torder_by, tfilter=tfilter, inherit=inherit)

Retrieve ranges.

Use this method to retrieve __Range__ objects. A __Range__ object represents a set of contiguous IP addresses in the same IP space with no gap, expressed as a (start, end) pair within a given subnet that are grouped together for administrative purpose and protocol management. The start and end values are not required to align with CIDR boundaries.

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
    api_instance = ipam.RangeApi(api_client)

    try:
        # Retrieve ranges.
        api_response = api_instance.list()
        pprint("The response of RangeApi->list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling RangeApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **torder_by** | **str**| This parameter is used for sorting by tags. | [optional] 
 **tfilter** | **str**| This parameter is used for filtering by tags. | [optional] 
 **inherit** | **str**| This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none | [optional] 

### Return type

[**ListRangeResponse**](ListRangeResponse.md)

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
    api_instance = ipam.RangeApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Retrieve the next available IP address.
        api_response = api_instance.list_next_available_ip(id)
        pprint("The response of RangeApi->list_next_available_ip:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling RangeApi->list_next_available_ip: %s\n" % e)
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

# **read**
> ReadRangeResponse read(id, fields=fields, inherit=inherit)

Retrieve the range.

Use this method to retrieve a __Range__ object. A __Range__ object represents a set of contiguous IP addresses in the same IP space with no gap, expressed as a (start, end) pair within a given subnet that are grouped together for administrative purpose and protocol management. The start and end values are not required to align with CIDR boundaries.

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
    api_instance = ipam.RangeApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Retrieve the range.
        api_response = api_instance.read(id)
        pprint("The response of RangeApi->read:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling RangeApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **inherit** | **str**| This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none | [optional] 

### Return type

[**ReadRangeResponse**](ReadRangeResponse.md)

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
> UpdateRangeResponse update(id, body, inherit=inherit)

Update the range.

Use this method to update a __Range__ object. A __Range__ object represents a set of contiguous IP addresses in the same IP space with no gap, expressed as a (start, end) pair within a given subnet that are grouped together for administrative purpose and protocol management. The start and end values are not required to align with CIDR boundaries.

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
    api_instance = ipam.RangeApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = ipam.Range() # Range | 

    try:
        # Update the range.
        api_response = api_instance.update(id, body)
        pprint("The response of RangeApi->update:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling RangeApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**Range**](Range.md)|  | 
 **inherit** | **str**| This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none | [optional] 

### Return type

[**UpdateRangeResponse**](UpdateRangeResponse.md)

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

