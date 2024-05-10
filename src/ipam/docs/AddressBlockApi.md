# ipam.AddressBlockApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Copy**](AddressBlockApi.md#Copy) | **POST** /ipam/address_block/{id}/copy | Copy the address block.
[**Create**](AddressBlockApi.md#Create) | **POST** /ipam/address_block | Create the address block.
[**CreateNextAvailableAB**](AddressBlockApi.md#CreateNextAvailableAB) | **POST** /ipam/address_block/{id}/nextavailableaddressblock | Create the Next Available Address Block object.
[**CreateNextAvailableIP**](AddressBlockApi.md#CreateNextAvailableIP) | **POST** /ipam/address_block/{id}/nextavailableip | Allocate the next available IP address.
[**CreateNextAvailableSubnet**](AddressBlockApi.md#CreateNextAvailableSubnet) | **POST** /ipam/address_block/{id}/nextavailablesubnet | Create the Next Available Subnet object.
[**Delete**](AddressBlockApi.md#Delete) | **DELETE** /ipam/address_block/{id} | Move the address block to the recycle bin.
[**List**](AddressBlockApi.md#List) | **GET** /ipam/address_block | Retrieve the address blocks.
[**ListNextAvailableAB**](AddressBlockApi.md#ListNextAvailableAB) | **GET** /ipam/address_block/{id}/nextavailableaddressblock | List Next Available Address Block objects.
[**ListNextAvailableIP**](AddressBlockApi.md#ListNextAvailableIP) | **GET** /ipam/address_block/{id}/nextavailableip | Retrieve the next available IP address.
[**ListNextAvailableSubnet**](AddressBlockApi.md#ListNextAvailableSubnet) | **GET** /ipam/address_block/{id}/nextavailablesubnet | List Next Available Subnet objects.
[**Read**](AddressBlockApi.md#Read) | **GET** /ipam/address_block/{id} | Retrieve the address block.
[**Update**](AddressBlockApi.md#Update) | **PATCH** /ipam/address_block/{id} | Update the address block.


# **Copy**
> CopyAddressBlockResponse Copy(id, body)

Copy the address block.

Use this method to copy an __AddressBlock__ object. The __AddressBlock__ object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.copy_address_block import CopyAddressBlock
from ipam.models.copy_address_block_response import CopyAddressBlockResponse
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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = ipam.CopyAddressBlock() # CopyAddressBlock | 

    try:
        # Copy the address block.
        api_response = api_instance.Copy(id, body)
        print("The response of AddressBlockApi->Copy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBlockApi->Copy: %s\n" % e)
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

# **Create**
> CreateAddressBlockResponse Create(body, inherit=inherit)

Create the address block.

Use this method to create an __AddressBlock__ object. The __AddressBlock__ object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.address_block import AddressBlock
from ipam.models.create_address_block_response import CreateAddressBlockResponse
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
    api_instance = ipam.AddressBlockApi(api_client)
    body = ipam.AddressBlock() # AddressBlock | 
    inherit = 'inherit_example' # str | This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none (optional)

    try:
        # Create the address block.
        api_response = api_instance.Create(body, inherit=inherit)
        print("The response of AddressBlockApi->Create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBlockApi->Create: %s\n" % e)
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

# **CreateNextAvailableAB**
> CreateNextAvailableABResponse CreateNextAvailableAB(id, cidr, count=count, name=name, comment=comment)

Create the Next Available Address Block object.

Use this method to create a Next Available __AddressBlock__ object. The Next Available Address Block is a generator that allocates one or more _ipam/address_block_ resource from available address blocks when the network address is not known prior to allocation.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.create_next_available_ab_response import CreateNextAvailableABResponse
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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    cidr = 56 # int | The cidr value of address blocks to be created.
    count = 1 # int | Number of address blocks to generate. Default 1 if not set. (optional) (default to 1)
    name = 'name_example' # str | Name of next available address blocks. (optional)
    comment = 'comment_example' # str | Comment of next available address blocks. (optional)

    try:
        # Create the Next Available Address Block object.
        api_response = api_instance.CreateNextAvailableAB(id, cidr, count=count, name=name, comment=comment)
        print("The response of AddressBlockApi->CreateNextAvailableAB:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBlockApi->CreateNextAvailableAB: %s\n" % e)
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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    contiguous = False # bool | Indicates whether the IP addresses should belong to a contiguous block.  Defaults to _false_. (optional) (default to False)
    count = 1 # int | The number of IP addresses requested.  Defaults to 1. (optional) (default to 1)

    try:
        # Allocate the next available IP address.
        api_response = api_instance.CreateNextAvailableIP(id, contiguous=contiguous, count=count)
        print("The response of AddressBlockApi->CreateNextAvailableIP:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBlockApi->CreateNextAvailableIP: %s\n" % e)
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

# **CreateNextAvailableSubnet**
> CreateNextAvailableSubnetResponse CreateNextAvailableSubnet(id, cidr, count=count, name=name, comment=comment, dhcp_host=dhcp_host)

Create the Next Available Subnet object.

Use this method to create a Next Available __Subnet__ object. The Next Available Subnet is a generator that allocates one or more _ipam/subnet_ resource from available subnets when the network address is not known prior to allocation.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.create_next_available_subnet_response import CreateNextAvailableSubnetResponse
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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    cidr = 56 # int | The cidr value of subnets to be created.
    count = 1 # int | Number of subnets to generate. Default 1 if not set. (optional) (default to 1)
    name = 'name_example' # str | Name of next available subnets. (optional)
    comment = 'comment_example' # str | Comment of next available subnets. (optional)
    dhcp_host = 'dhcp_host_example' # str | Reference of OnPrem Host associated with the next available subnets to be created. (optional)

    try:
        # Create the Next Available Subnet object.
        api_response = api_instance.CreateNextAvailableSubnet(id, cidr, count=count, name=name, comment=comment, dhcp_host=dhcp_host)
        print("The response of AddressBlockApi->CreateNextAvailableSubnet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBlockApi->CreateNextAvailableSubnet: %s\n" % e)
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

# **Delete**
> Delete(id)

Move the address block to the recycle bin.

Use this method to move an __AddressBlock__ object to the recycle bin. The __AddressBlock__ object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Move the address block to the recycle bin.
        api_instance.Delete(id)
    except Exception as e:
        print("Exception when calling AddressBlockApi->Delete: %s\n" % e)
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
> ListAddressBlockResponse List(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, torder_by=torder_by, tfilter=tfilter, inherit=inherit)

Retrieve the address blocks.

Use this method to retrieve __AddressBlock__ objects. The __AddressBlock__ object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.list_address_block_response import ListAddressBlockResponse
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
    api_instance = ipam.AddressBlockApi(api_client)
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
        # Retrieve the address blocks.
        api_response = api_instance.List(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, torder_by=torder_by, tfilter=tfilter, inherit=inherit)
        print("The response of AddressBlockApi->List:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBlockApi->List: %s\n" % e)
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

# **ListNextAvailableAB**
> NextAvailableABResponse ListNextAvailableAB(id, cidr=cidr, count=count, name=name, comment=comment)

List Next Available Address Block objects.

Use this method to list Next Available __AddressBlock__ objects. The Next Available __AddressBlock__ is a generator that returns one or more _ipam/address_block_ resource from available address blocks when the network address is not known prior to allocation.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.next_available_ab_response import NextAvailableABResponse
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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    cidr = 56 # int | The cidr value of address blocks to be created. (optional)
    count = 56 # int | Number of address blocks to generate. Default 1 if not set. (optional)
    name = 'name_example' # str | Name of next available address blocks. (optional)
    comment = 'comment_example' # str | Comment of next available address blocks. (optional)

    try:
        # List Next Available Address Block objects.
        api_response = api_instance.ListNextAvailableAB(id, cidr=cidr, count=count, name=name, comment=comment)
        print("The response of AddressBlockApi->ListNextAvailableAB:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBlockApi->ListNextAvailableAB: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **cidr** | **int**| The cidr value of address blocks to be created. | [optional] 
 **count** | **int**| Number of address blocks to generate. Default 1 if not set. | [optional] 
 **name** | **str**| Name of next available address blocks. | [optional] 
 **comment** | **str**| Comment of next available address blocks. | [optional] 

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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    contiguous = True # bool | Indicates whether the IP addresses should belong to a contiguous block.  Defaults to _false_. (optional)
    count = 56 # int | The number of IP addresses requested.  Defaults to 1. (optional)

    try:
        # Retrieve the next available IP address.
        api_response = api_instance.ListNextAvailableIP(id, contiguous=contiguous, count=count)
        print("The response of AddressBlockApi->ListNextAvailableIP:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBlockApi->ListNextAvailableIP: %s\n" % e)
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

# **ListNextAvailableSubnet**
> NextAvailableSubnetResponse ListNextAvailableSubnet(id, cidr=cidr, count=count, name=name, comment=comment, dhcp_host=dhcp_host)

List Next Available Subnet objects.

Use this method to list Next Available __Subnet__ objects. The Next Available Address Block is a generator that returns one or more _ipam/subnet_ resource from available subnets when the network address is not known prior to allocation.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.next_available_subnet_response import NextAvailableSubnetResponse
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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    cidr = 56 # int | The cidr value of subnets to be created. (optional)
    count = 56 # int | Number of subnets to generate. Default 1 if not set. (optional)
    name = 'name_example' # str | Name of next available subnets. (optional)
    comment = 'comment_example' # str | Comment of next available subnets. (optional)
    dhcp_host = 'dhcp_host_example' # str | Reference of OnPrem Host associated with the next available subnets to be created. (optional)

    try:
        # List Next Available Subnet objects.
        api_response = api_instance.ListNextAvailableSubnet(id, cidr=cidr, count=count, name=name, comment=comment, dhcp_host=dhcp_host)
        print("The response of AddressBlockApi->ListNextAvailableSubnet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBlockApi->ListNextAvailableSubnet: %s\n" % e)
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

# **Read**
> ReadAddressBlockResponse Read(id, fields=fields, inherit=inherit)

Retrieve the address block.

Use this method to retrieve an __AddressBlock__ object. The __AddressBlock__ object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.read_address_block_response import ReadAddressBlockResponse
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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    inherit = 'inherit_example' # str | This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none (optional)

    try:
        # Retrieve the address block.
        api_response = api_instance.Read(id, fields=fields, inherit=inherit)
        print("The response of AddressBlockApi->Read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBlockApi->Read: %s\n" % e)
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

# **Update**
> UpdateAddressBlockResponse Update(id, body, inherit=inherit)

Update the address block.

Use this method to update an __AddressBlock__ object. The __AddressBlock__ object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipam
from ipam.models.address_block import AddressBlock
from ipam.models.update_address_block_response import UpdateAddressBlockResponse
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
    api_instance = ipam.AddressBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = ipam.AddressBlock() # AddressBlock | 
    inherit = 'inherit_example' # str | This parameter is used for getting inheritance_sources.  Allowed values: * _none_, * _partial_, * _full_.  Defaults to _none (optional)

    try:
        # Update the address block.
        api_response = api_instance.Update(id, body, inherit=inherit)
        print("The response of AddressBlockApi->Update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBlockApi->Update: %s\n" % e)
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

