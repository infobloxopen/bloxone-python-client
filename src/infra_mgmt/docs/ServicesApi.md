# infra_mgmt.ServicesApi

All URIs are relative to *http://csp.infoblox.com/api/infra/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Applications**](ServicesApi.md#Applications) | **GET** /applications | List applications (Service types) for a particular account.
[**Create**](ServicesApi.md#Create) | **POST** /services | Create a Service resource.
[**Delete**](ServicesApi.md#Delete) | **DELETE** /services/{id} | Delete a Service resource.
[**List**](ServicesApi.md#List) | **GET** /services | List all the Service resources for an account.
[**Read**](ServicesApi.md#Read) | **GET** /services/{id} | Read a Service resource.
[**Update**](ServicesApi.md#Update) | **PUT** /services/{id} | Update a Service resource.


# **Applications**
> ApplicationsResponse Applications(account_id=account_id)

List applications (Service types) for a particular account.

Used in order to retrieve available applications (Service types) for a particular account.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.models.applications_response import ApplicationsResponse
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.ServicesApi(api_client)
    account_id = 'account_id_example' # str | Account ID. (optional)

    try:
        # List applications (Service types) for a particular account.
        api_response = api_instance.Applications(account_id=account_id)
        print("The response of ServicesApi->Applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->Applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID. | [optional] 

### Return type

[**ApplicationsResponse**](ApplicationsResponse.md)

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

# **Create**
> CreateServiceResponse Create(body)

Create a Service resource.

Validation: - \"name\" is required and should be unique. - \"service_type\" is required. - \"pool_id\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.models.create_service_response import CreateServiceResponse
from infra_mgmt.models.service import Service
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.ServicesApi(api_client)
    body = infra_mgmt.Service() # Service | 

    try:
        # Create a Service resource.
        api_response = api_instance.Create(body)
        print("The response of ServicesApi->Create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->Create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Service**](Service.md)|  | 

### Return type

[**CreateServiceResponse**](CreateServiceResponse.md)

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

# **Delete**
> Delete(id)

Delete a Service resource.

Validation: - \"id\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.ServicesApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Delete a Service resource.
        api_instance.Delete(id)
    except Exception as e:
        print("Exception when calling ServicesApi->Delete: %s\n" % e)
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **List**
> ListServiceResponse List(filter=filter, order_by=order_by, offset=offset, limit=limit, page_token=page_token, fields=fields, tfilter=tfilter, torder_by=torder_by)

List all the Service resources for an account.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.models.list_service_response import ListServiceResponse
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.ServicesApi(api_client)
    filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)
    order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
    offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
    limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
    page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
    tfilter = 'tfilter_example' # str | This parameter is used for filtering by tags. (optional)
    torder_by = 'torder_by_example' # str | This parameter is used for sorting by tags. (optional)

    try:
        # List all the Service resources for an account.
        api_response = api_instance.List(filter=filter, order_by=order_by, offset=offset, limit=limit, page_token=page_token, fields=fields, tfilter=tfilter, torder_by=torder_by)
        print("The response of ServicesApi->List:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->List: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **tfilter** | **str**| This parameter is used for filtering by tags. | [optional] 
 **torder_by** | **str**| This parameter is used for sorting by tags. | [optional] 

### Return type

[**ListServiceResponse**](ListServiceResponse.md)

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
> GetServiceResponse Read(id)

Read a Service resource.

Validation: - \"id\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.models.get_service_response import GetServiceResponse
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.ServicesApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Read a Service resource.
        api_response = api_instance.Read(id)
        print("The response of ServicesApi->Read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->Read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 

### Return type

[**GetServiceResponse**](GetServiceResponse.md)

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
> UpdateServiceResponse Update(id, body)

Update a Service resource.

Validation: - \"id\" is required. - \"name\" is required and should be unique. - \"service_type\" is required. - \"pool_id\" is required.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_mgmt
from infra_mgmt.models.service import Service
from infra_mgmt.models.update_service_response import UpdateServiceResponse
from infra_mgmt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/infra/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_mgmt.Configuration(
    host = "http://csp.infoblox.com/api/infra/v1"
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
with infra_mgmt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_mgmt.ServicesApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = infra_mgmt.Service() # Service | 

    try:
        # Update a Service resource.
        api_response = api_instance.Update(id, body)
        print("The response of ServicesApi->Update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->Update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**Service**](Service.md)|  | 

### Return type

[**UpdateServiceResponse**](UpdateServiceResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PUT operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

