# infra_provision.UICSRApi

All URIs are relative to *http://csp.infoblox.com/host-activation/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Approve**](UICSRApi.md#Approve) | **POST** /csr/{activation_code}/approve | Marks the certificate signing request as approved. The host activation service will then continue with the signing process.
[**Deny**](UICSRApi.md#Deny) | **POST** /csr/{activation_code}/deny | Marks the certificate signing request as denied.
[**List**](UICSRApi.md#List) | **GET** /csr | User can list the certificate signing requests for an account.
[**Revoke**](UICSRApi.md#Revoke) | **POST** /cert/{cert_serial}/revoke | Invalidates a certificate by adding it to a certificate revocation list.
[**Revoke2**](UICSRApi.md#Revoke2) | **POST** /host/{ophid}/revoke | Invalidates a certificate by adding it to a certificate revocation list.


# **Approve**
> object Approve(activation_code, body)

Marks the certificate signing request as approved. The host activation service will then continue with the signing process.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_provision
from infra_provision.models.approve_csr_request import ApproveCSRRequest
from infra_provision.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/host-activation/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_provision.Configuration(
    host = "http://csp.infoblox.com/host-activation/v1"
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
with infra_provision.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UICSRApi(api_client)
    activation_code = 'activation_code_example' # str | activation code is used by the clients to track the approval of the CSR
    body = infra_provision.ApproveCSRRequest() # ApproveCSRRequest | 

    try:
        # Marks the certificate signing request as approved. The host activation service will then continue with the signing process.
        api_response = api_instance.Approve(activation_code, body)
        print("The response of UICSRApi->Approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UICSRApi->Approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_code** | **str**| activation code is used by the clients to track the approval of the CSR | 
 **body** | [**ApproveCSRRequest**](ApproveCSRRequest.md)|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Deny**
> object Deny(activation_code, body)

Marks the certificate signing request as denied.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_provision
from infra_provision.models.deny_csr_request import DenyCSRRequest
from infra_provision.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/host-activation/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_provision.Configuration(
    host = "http://csp.infoblox.com/host-activation/v1"
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
with infra_provision.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UICSRApi(api_client)
    activation_code = 'activation_code_example' # str | activation code is used by the clients to track the approval of the CSR
    body = infra_provision.DenyCSRRequest() # DenyCSRRequest | 

    try:
        # Marks the certificate signing request as denied.
        api_response = api_instance.Deny(activation_code, body)
        print("The response of UICSRApi->Deny:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UICSRApi->Deny: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_code** | **str**| activation code is used by the clients to track the approval of the CSR | 
 **body** | [**DenyCSRRequest**](DenyCSRRequest.md)|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **List**
> ListCSRsResponse List(filter=filter, order_by=order_by, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)

User can list the certificate signing requests for an account.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_provision
from infra_provision.models.list_csrs_response import ListCSRsResponse
from infra_provision.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/host-activation/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_provision.Configuration(
    host = "http://csp.infoblox.com/host-activation/v1"
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
with infra_provision.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UICSRApi(api_client)
    filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)
    order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
    offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
    limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
    page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
    tfilter = 'tfilter_example' # str | This parameter is used for filtering by tags. (optional)
    torder_by = 'torder_by_example' # str | This parameter is used for sorting by tags. (optional)

    try:
        # User can list the certificate signing requests for an account.
        api_response = api_instance.List(filter=filter, order_by=order_by, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)
        print("The response of UICSRApi->List:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UICSRApi->List: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **tfilter** | **str**| This parameter is used for filtering by tags. | [optional] 
 **torder_by** | **str**| This parameter is used for sorting by tags. | [optional] 

### Return type

[**ListCSRsResponse**](ListCSRsResponse.md)

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

# **Revoke**
> object Revoke(cert_serial, body)

Invalidates a certificate by adding it to a certificate revocation list.

The user can revoke the cert from the cloud (for example, if in case a host is compromised). Validation: - one of \"cert_serial\" or \"ophid\" should be provided - \"revoke_reason\" is optional

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_provision
from infra_provision.models.revoke_cert_request import RevokeCertRequest
from infra_provision.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/host-activation/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_provision.Configuration(
    host = "http://csp.infoblox.com/host-activation/v1"
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
with infra_provision.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UICSRApi(api_client)
    cert_serial = 'cert_serial_example' # str | x509 serial number of the certificate. This can be obtained by parsing the client certificate file on the onprem. Either cert_serial or ophid is required
    body = infra_provision.RevokeCertRequest() # RevokeCertRequest | 

    try:
        # Invalidates a certificate by adding it to a certificate revocation list.
        api_response = api_instance.Revoke(cert_serial, body)
        print("The response of UICSRApi->Revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UICSRApi->Revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_serial** | **str**| x509 serial number of the certificate. This can be obtained by parsing the client certificate file on the onprem. Either cert_serial or ophid is required | 
 **body** | [**RevokeCertRequest**](RevokeCertRequest.md)|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Revoke2**
> object Revoke2(ophid, body)

Invalidates a certificate by adding it to a certificate revocation list.

The user can revoke the cert from the cloud (for example, if in case a host is compromised). Validation: - one of \"cert_serial\" or \"ophid\" should be provided - \"revoke_reason\" is optional

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import infra_provision
from infra_provision.models.revoke_cert_request import RevokeCertRequest
from infra_provision.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/host-activation/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = infra_provision.Configuration(
    host = "http://csp.infoblox.com/host-activation/v1"
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
with infra_provision.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infra_provision.UICSRApi(api_client)
    ophid = 'ophid_example' # str | On-prem host ID which can be obtained either from on-prem or BloxOne UI portal(Manage > Infrastructure > Hosts > Select the onprem > click on 3 dots on top right side > General Information > Ophid) .
    body = infra_provision.RevokeCertRequest() # RevokeCertRequest | 

    try:
        # Invalidates a certificate by adding it to a certificate revocation list.
        api_response = api_instance.Revoke2(ophid, body)
        print("The response of UICSRApi->Revoke2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UICSRApi->Revoke2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ophid** | **str**| On-prem host ID which can be obtained either from on-prem or BloxOne UI portal(Manage &gt; Infrastructure &gt; Hosts &gt; Select the onprem &gt; click on 3 dots on top right side &gt; General Information &gt; Ophid) . | 
 **body** | [**RevokeCertRequest**](RevokeCertRequest.md)|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

