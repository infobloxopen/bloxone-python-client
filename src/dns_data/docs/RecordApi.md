# dns_data.RecordApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](RecordApi.md#create) | **POST** /dns/record | Create the DNS resource record.
[**delete**](RecordApi.md#delete) | **DELETE** /dns/record/{id} | Move the DNS resource record to recycle bin.
[**list**](RecordApi.md#list) | **GET** /dns/record | Retrieve DNS resource records.
[**read**](RecordApi.md#read) | **GET** /dns/record/{id} | Retrieve the DNS resource record.
[**soa_serial_increment**](RecordApi.md#soa_serial_increment) | **POST** /dns/record/{id}/serial_increment | Increment serial number for the SOA record.
[**update**](RecordApi.md#update) | **PATCH** /dns/record/{id} | Update the DNS resource record.


# **create**
> CreateRecordResponse create(body, inherit=inherit)

Create the DNS resource record.

Use this method to create a DNS __Record__ object. A __Record__ object represents a DNS resource record in an authoritative zone.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import dns_data

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = dns_data.RecordApi(api_client)
    body = dns_data.Record() # Record | 

    try:
        # Create the DNS resource record.
        api_response = api_instance.create(body)
        pprint("The response of RecordApi->create:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling RecordApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Record**](Record.md)|  | 
 **inherit** | **str**| This parameter is used for getting inheritance_sources. | [optional] 

### Return type

[**CreateRecordResponse**](CreateRecordResponse.md)

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

Move the DNS resource record to recycle bin.

Use this method to move a DNS __Record__ object to the recycle bin. A __Record__ object represents a DNS resource record in an authoritative zone.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import dns_data

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = dns_data.RecordApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Move the DNS resource record to recycle bin.
        api_instance.delete(id)
    except Exception as e:
        pprint("Exception when calling RecordApi->delete: %s\n" % e)
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
> ListRecordResponse list(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, tfilter=tfilter, torder_by=torder_by, inherit=inherit)

Retrieve DNS resource records.

Use this method to retrieve DNS __Record__ objects. A __Record__ object represents a DNS resource record in an authoritative zone.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import dns_data

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = dns_data.RecordApi(api_client)

    try:
        # Retrieve DNS resource records.
        api_response = api_instance.list()
        pprint("The response of RecordApi->list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling RecordApi->list: %s\n" % e)
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
 **tfilter** | **str**| This parameter is used for filtering by tags. | [optional] 
 **torder_by** | **str**| This parameter is used for sorting by tags. | [optional] 
 **inherit** | **str**| This parameter is used for getting inheritance_sources. | [optional] 

### Return type

[**ListRecordResponse**](ListRecordResponse.md)

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
> ReadRecordResponse read(id, fields=fields, inherit=inherit)

Retrieve the DNS resource record.

Use this method to retrieve a DNS __Record__ object. A __Record__ object represents a DNS resource record in an authoritative zone.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import dns_data

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = dns_data.RecordApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Retrieve the DNS resource record.
        api_response = api_instance.read(id)
        pprint("The response of RecordApi->read:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling RecordApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **inherit** | **str**| This parameter is used for getting inheritance_sources. | [optional] 

### Return type

[**ReadRecordResponse**](ReadRecordResponse.md)

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

# **soa_serial_increment**
> SOASerialIncrementResponse soa_serial_increment(id, body)

Increment serial number for the SOA record.

Use this method to increment the serial number for an SOA (Start of Authority) _Record_ object. A __Record__ object represents a DNS resource record in an authoritative zone.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import dns_data

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = dns_data.RecordApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = dns_data.SOASerialIncrementRequest() # SOASerialIncrementRequest | 

    try:
        # Increment serial number for the SOA record.
        api_response = api_instance.soa_serial_increment(id, body)
        pprint("The response of RecordApi->soa_serial_increment:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling RecordApi->soa_serial_increment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**SOASerialIncrementRequest**](SOASerialIncrementRequest.md)|  | 

### Return type

[**SOASerialIncrementResponse**](SOASerialIncrementResponse.md)

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

# **update**
> UpdateRecordResponse update(id, body, inherit=inherit)

Update the DNS resource record.

Use this method to update a DNS __Record__ object. A __Record__ object represents a DNS resource record in an authoritative zone.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import dns_data

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = dns_data.RecordApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = dns_data.Record() # Record | 

    try:
        # Update the DNS resource record.
        api_response = api_instance.update(id, body)
        pprint("The response of RecordApi->update:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling RecordApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**Record**](Record.md)|  | 
 **inherit** | **str**| This parameter is used for getting inheritance_sources. | [optional] 

### Return type

[**UpdateRecordResponse**](UpdateRecordResponse.md)

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

