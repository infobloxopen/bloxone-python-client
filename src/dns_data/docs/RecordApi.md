# dns_data.RecordApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Create**](RecordApi.md#Create) | **POST** /dns/record | Create the DNS resource record.
[**Delete**](RecordApi.md#Delete) | **DELETE** /dns/record/{id} | Move the DNS resource record to recycle bin.
[**List**](RecordApi.md#List) | **GET** /dns/record | Retrieve DNS resource records.
[**Read**](RecordApi.md#Read) | **GET** /dns/record/{id} | Retrieve the DNS resource record.
[**SOASerialIncrement**](RecordApi.md#SOASerialIncrement) | **POST** /dns/record/{id}/serial_increment | Increment serial number for the SOA record.
[**Update**](RecordApi.md#Update) | **PATCH** /dns/record/{id} | Update the DNS resource record.


# **Create**
> CreateRecordResponse Create(body, inherit=inherit)

Create the DNS resource record.

Use this method to create a DNS __Record__ object. A __Record__ object represents a DNS resource record in an authoritative zone.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dns_data
from dns_data.models.create_record_response import CreateRecordResponse
from dns_data.models.record import Record
from dns_data.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dns_data.Configuration(
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
with dns_data.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dns_data.RecordApi(api_client)
    body = dns_data.Record() # Record | 
    inherit = 'inherit_example' # str | This parameter is used for getting inheritance_sources. (optional)

    try:
        # Create the DNS resource record.
        api_response = api_instance.Create(body, inherit=inherit)
        print("The response of RecordApi->Create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordApi->Create: %s\n" % e)
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

# **Delete**
> Delete(id)

Move the DNS resource record to recycle bin.

Use this method to move a DNS __Record__ object to the recycle bin. A __Record__ object represents a DNS resource record in an authoritative zone.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dns_data
from dns_data.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dns_data.Configuration(
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
with dns_data.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dns_data.RecordApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Move the DNS resource record to recycle bin.
        api_instance.Delete(id)
    except Exception as e:
        print("Exception when calling RecordApi->Delete: %s\n" % e)
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

# **List**
> ListRecordResponse List(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, tfilter=tfilter, torder_by=torder_by, inherit=inherit)

Retrieve DNS resource records.

Use this method to retrieve DNS __Record__ objects. A __Record__ object represents a DNS resource record in an authoritative zone.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dns_data
from dns_data.models.list_record_response import ListRecordResponse
from dns_data.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dns_data.Configuration(
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
with dns_data.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dns_data.RecordApi(api_client)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)
    offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
    limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
    page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
    order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
    tfilter = 'tfilter_example' # str | This parameter is used for filtering by tags. (optional)
    torder_by = 'torder_by_example' # str | This parameter is used for sorting by tags. (optional)
    inherit = 'inherit_example' # str | This parameter is used for getting inheritance_sources. (optional)

    try:
        # Retrieve DNS resource records.
        api_response = api_instance.List(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, tfilter=tfilter, torder_by=torder_by, inherit=inherit)
        print("The response of RecordApi->List:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordApi->List: %s\n" % e)
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

# **Read**
> ReadRecordResponse Read(id, fields=fields, inherit=inherit)

Retrieve the DNS resource record.

Use this method to retrieve a DNS __Record__ object. A __Record__ object represents a DNS resource record in an authoritative zone.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dns_data
from dns_data.models.read_record_response import ReadRecordResponse
from dns_data.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dns_data.Configuration(
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
with dns_data.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dns_data.RecordApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    inherit = 'inherit_example' # str | This parameter is used for getting inheritance_sources. (optional)

    try:
        # Retrieve the DNS resource record.
        api_response = api_instance.Read(id, fields=fields, inherit=inherit)
        print("The response of RecordApi->Read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordApi->Read: %s\n" % e)
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

# **SOASerialIncrement**
> SOASerialIncrementResponse SOASerialIncrement(id, body)

Increment serial number for the SOA record.

Use this method to increment the serial number for an SOA (Start of Authority) _Record_ object. A __Record__ object represents a DNS resource record in an authoritative zone.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dns_data
from dns_data.models.soa_serial_increment_request import SOASerialIncrementRequest
from dns_data.models.soa_serial_increment_response import SOASerialIncrementResponse
from dns_data.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dns_data.Configuration(
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
with dns_data.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dns_data.RecordApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = dns_data.SOASerialIncrementRequest() # SOASerialIncrementRequest | 

    try:
        # Increment serial number for the SOA record.
        api_response = api_instance.SOASerialIncrement(id, body)
        print("The response of RecordApi->SOASerialIncrement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordApi->SOASerialIncrement: %s\n" % e)
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

# **Update**
> UpdateRecordResponse Update(id, body, inherit=inherit)

Update the DNS resource record.

Use this method to update a DNS __Record__ object. A __Record__ object represents a DNS resource record in an authoritative zone.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dns_data
from dns_data.models.record import Record
from dns_data.models.update_record_response import UpdateRecordResponse
from dns_data.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dns_data.Configuration(
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
with dns_data.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dns_data.RecordApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = dns_data.Record() # Record | 
    inherit = 'inherit_example' # str | This parameter is used for getting inheritance_sources. (optional)

    try:
        # Update the DNS resource record.
        api_response = api_instance.Update(id, body, inherit=inherit)
        print("The response of RecordApi->Update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordApi->Update: %s\n" % e)
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

