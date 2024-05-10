# ipam.SubnetApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Copy**](SubnetApi.md#Copy) | **POST** /ipam/subnet/{id}/copy | Copy the subnet.
[**Create**](SubnetApi.md#Create) | **POST** /ipam/subnet | Create the subnet.
[**CreateNextAvailableIP**](SubnetApi.md#CreateNextAvailableIP) | **POST** /ipam/subnet/{id}/nextavailableip | Allocate the next available IP address.
[**Delete**](SubnetApi.md#Delete) | **DELETE** /ipam/subnet/{id} | Move the subnet to the recycle bin.
[**List**](SubnetApi.md#List) | **GET** /ipam/subnet | Retrieve subnets.
[**ListNextAvailableIP**](SubnetApi.md#ListNextAvailableIP) | **GET** /ipam/subnet/{id}/nextavailableip | Retrieve the next available IP address.
[**Read**](SubnetApi.md#Read) | **GET** /ipam/subnet/{id} | Retrieve the subnet.
[**Update**](SubnetApi.md#Update) | **PATCH** /ipam/subnet/{id} | Update the subnet.


# **Copy**
> CopySubnetResponse Copy(id, body)

Copy the subnet.

Use this method to copy a __Subnet__ object. The __Subnet__ object represents a set of addresses from which addresses are assigned to network equipment interfaces.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.copy_subnet import CopySubnet
from ipam.models.copy_subnet_response import CopySubnetResponse
from ipam.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ipam.Configuration(
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
with ipam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipam.SubnetApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = ipam.CopySubnet() # CopySubnet | 

    try:
        # Copy the subnet.
        api_response = api_instance.Copy(id, body)
        print("The response of SubnetApi->Copy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubnetApi->Copy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**CopySubnet**](CopySubnet.md)|  | 

### Return type

[**CopySubnetResponse**](CopySubnetResponse.md)

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

# **Create**
> CreateSubnetResponse Create(body, inherit=inherit)

Create the subnet.

Use this method to create a __Subnet__ object. The __Subnet__ object represents a set of addresses from which addresses are assigned to network equipment interfaces.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.create_subnet_response import CreateSubnetResponse
from ipam.models.subnet import Subnet
from ipam.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ipam.Configuration(
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
with ipam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipam.SubnetApi(api_client)
    body = ipam.Subnet() # Subnet | 
    inherit = 'inherit_example' # str | This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none (optional)

    try:
        # Create the subnet.
        api_response = api_instance.Create(body, inherit=inherit)
        print("The response of SubnetApi->Create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubnetApi->Create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Subnet**](Subnet.md)|  | 
 **inherit** | **str**| This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none | [optional] 

### Return type

[**CreateSubnetResponse**](CreateSubnetResponse.md)

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

# **CreateNextAvailableIP**
> CreateNextAvailableIPResponse CreateNextAvailableIP(id, contiguous=contiguous, count=count)

Allocate the next available IP address.

Use this method to allocate the next available IP address. This allocates one or more __Address__ (_ipam/address_) resource from available addresses, when the IP address is not known prior to allocation.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.create_next_available_ip_response import CreateNextAvailableIPResponse
from ipam.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ipam.Configuration(
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
with ipam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipam.SubnetApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    contiguous = False # bool | Indicates whether the IP addresses should belong to a contiguous block.  Defaults to _false_. (optional) (default to False)
    count = 1 # int | The number of IP addresses requested.  Defaults to 1. (optional) (default to 1)

    try:
        # Allocate the next available IP address.
        api_response = api_instance.CreateNextAvailableIP(id, contiguous=contiguous, count=count)
        print("The response of SubnetApi->CreateNextAvailableIP:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubnetApi->CreateNextAvailableIP: %s\n" % e)
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

# **Delete**
> Delete(id)

Move the subnet to the recycle bin.

Use this method to move a __Subnet__ object to the recycle bin. The __Subnet__ object represents a set of addresses from which addresses are assigned to network equipment interfaces.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ipam.Configuration(
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
with ipam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipam.SubnetApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Move the subnet to the recycle bin.
        api_instance.Delete(id)
    except Exception as e:
        print("Exception when calling SubnetApi->Delete: %s\n" % e)
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
> ListSubnetResponse List(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, torder_by=torder_by, tfilter=tfilter, inherit=inherit)

Retrieve subnets.

Use this method to retrieve __Subnet__ objects. The __Subnet__ object represents a set of addresses from which addresses are assigned to network equipment interfaces.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.list_subnet_response import ListSubnetResponse
from ipam.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ipam.Configuration(
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
with ipam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipam.SubnetApi(api_client)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)
    offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
    limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
    page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
    order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
    torder_by = 'torder_by_example' # str | This parameter is used for sorting by tags. (optional)
    tfilter = 'tfilter_example' # str | This parameter is used for filtering by tags. (optional)
    inherit = 'inherit_example' # str | This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none (optional)

    try:
        # Retrieve subnets.
        api_response = api_instance.List(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, torder_by=torder_by, tfilter=tfilter, inherit=inherit)
        print("The response of SubnetApi->List:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubnetApi->List: %s\n" % e)
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

[**ListSubnetResponse**](ListSubnetResponse.md)

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

# **ListNextAvailableIP**
> NextAvailableIPResponse ListNextAvailableIP(id, contiguous=contiguous, count=count)

Retrieve the next available IP address.

Use this method to retrieve the next available IP address. This returns one or more __Address__ (_ipam/address_) resource from available addresses, when IP address is not known prior to allocation.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.next_available_ip_response import NextAvailableIPResponse
from ipam.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ipam.Configuration(
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
with ipam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipam.SubnetApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    contiguous = True # bool | Indicates whether the IP addresses should belong to a contiguous block.  Defaults to _false_. (optional)
    count = 56 # int | The number of IP addresses requested.  Defaults to 1. (optional)

    try:
        # Retrieve the next available IP address.
        api_response = api_instance.ListNextAvailableIP(id, contiguous=contiguous, count=count)
        print("The response of SubnetApi->ListNextAvailableIP:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubnetApi->ListNextAvailableIP: %s\n" % e)
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

# **Read**
> ReadSubnetResponse Read(id, fields=fields, inherit=inherit)

Retrieve the subnet.

Use this method to retrieve a __Subnet__ object. The __Subnet__ object represents a set of addresses from which addresses are assigned to network equipment interfaces.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.read_subnet_response import ReadSubnetResponse
from ipam.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ipam.Configuration(
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
with ipam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipam.SubnetApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    inherit = 'inherit_example' # str | This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none (optional)

    try:
        # Retrieve the subnet.
        api_response = api_instance.Read(id, fields=fields, inherit=inherit)
        print("The response of SubnetApi->Read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubnetApi->Read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **inherit** | **str**| This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none | [optional] 

### Return type

[**ReadSubnetResponse**](ReadSubnetResponse.md)

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
> UpdateSubnetResponse Update(id, body, inherit=inherit)

Update the subnet.

Use this method to update a __Subnet__ object. The __Subnet__ object represents a set of addresses from which addresses are assigned to network equipment interfaces.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.subnet import Subnet
from ipam.models.update_subnet_response import UpdateSubnetResponse
from ipam.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ipam.Configuration(
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
with ipam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipam.SubnetApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = ipam.Subnet() # Subnet | 
    inherit = 'inherit_example' # str | This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none (optional)

    try:
        # Update the subnet.
        api_response = api_instance.Update(id, body, inherit=inherit)
        print("The response of SubnetApi->Update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubnetApi->Update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**Subnet**](Subnet.md)|  | 
 **inherit** | **str**| This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none | [optional] 

### Return type

[**UpdateSubnetResponse**](UpdateSubnetResponse.md)

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

