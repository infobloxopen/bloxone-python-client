# ipam.IpamHostApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](IpamHostApi.md#create) | **POST** /ipam/host | Create the IPAM host.
[**delete**](IpamHostApi.md#delete) | **DELETE** /ipam/host/{id} | Move the IPAM host to the recycle bin.
[**list**](IpamHostApi.md#list) | **GET** /ipam/host | Retrieve the IPAM hosts.
[**read**](IpamHostApi.md#read) | **GET** /ipam/host/{id} | Retrieve the IPAM host.
[**update**](IpamHostApi.md#update) | **PATCH** /ipam/host/{id} | Update the IPAM host.


# **create**
> CreateIpamHostResponse create(body)

Create the IPAM host.

Use this method to create an __IpamHost__ object. The __IpamHost__ object (_ipam/host_) represents any network connected equipment that is assigned one or more IP Addresses.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam

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
    api_instance = ipam.IpamHostApi(api_client)
    body = ipam.IpamHost() # IpamHost | 

    try:
        # Create the IPAM host.
        api_response = api_instance.create(body)
        pprint("The response of IpamHostApi->create:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling IpamHostApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpamHost**](IpamHost.md)|  | 

### Return type

[**CreateIpamHostResponse**](CreateIpamHostResponse.md)

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

# **delete**
> delete(id)

Move the IPAM host to the recycle bin.

Use this method to move an __IpamHost__ object to the recycle bin. The __IpamHost__ object (_ipam/host_) represents any network connected equipment that is assigned one or more IP Addresses.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam

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
    api_instance = ipam.IpamHostApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Move the IPAM host to the recycle bin.
        api_instance.delete(id)
    except Exception as e:
        pprint("Exception when calling IpamHostApi->delete: %s\n" % e)
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
> ListIpamHostResponse list(fields=fields, order_by=order_by, filter=filter, offset=offset, limit=limit, page_token=page_token, torder_by=torder_by, tfilter=tfilter)

Retrieve the IPAM hosts.

Use this method to retrieve __IpamHost__ objects. The __IpamHost__ object (_ipam/host_) represents any network connected equipment that is assigned one or more IP Addresses.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam

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
    api_instance = ipam.IpamHostApi(api_client)

    try:
        # Retrieve the IPAM hosts.
        api_response = api_instance.list()
        pprint("The response of IpamHostApi->list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling IpamHostApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **torder_by** | **str**| This parameter is used for sorting by tags. | [optional] 
 **tfilter** | **str**| This parameter is used for filtering by tags. | [optional] 

### Return type

[**ListIpamHostResponse**](ListIpamHostResponse.md)

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
> ReadIpamHostResponse read(id, order_by=order_by, fields=fields)

Retrieve the IPAM host.

Use this method to retrieve an __IpamHost__ object. The __IpamHost__ object (_ipam/host_) represents any network connected equipment that is assigned one or more IP Addresses.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam

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
    api_instance = ipam.IpamHostApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Retrieve the IPAM host.
        api_response = api_instance.read(id)
        pprint("The response of IpamHostApi->read:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling IpamHostApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**ReadIpamHostResponse**](ReadIpamHostResponse.md)

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
> UpdateIpamHostResponse update(id, body)

Update the IPAM host.

Use this method to update an __IpamHost__ object. The __IpamHost__ object (_ipam/host_) represents any network connected equipment that is assigned one or more IP Addresses.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam

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
    api_instance = ipam.IpamHostApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = ipam.IpamHost() # IpamHost | 

    try:
        # Update the IPAM host.
        api_response = api_instance.update(id, body)
        pprint("The response of IpamHostApi->update:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling IpamHostApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**IpamHost**](IpamHost.md)|  | 

### Return type

[**UpdateIpamHostResponse**](UpdateIpamHostResponse.md)

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

