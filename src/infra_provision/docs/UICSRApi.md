# infra_provision.UICSRApi

All URIs are relative to *http://csp.infoblox.com/host-activation/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve**](UICSRApi.md#approve) | **POST** /csr/{activation_code}/approve | Marks the certificate signing request as approved. The host activation service will then continue with the signing process.
[**deny**](UICSRApi.md#deny) | **POST** /csr/{activation_code}/deny | Marks the certificate signing request as denied.
[**list**](UICSRApi.md#list) | **GET** /csr | User can list the certificate signing requests for an account.
[**revoke**](UICSRApi.md#revoke) | **POST** /cert/{cert_serial}/revoke | Invalidates a certificate by adding it to a certificate revocation list.
[**revoke2**](UICSRApi.md#revoke2) | **POST** /host/{ophid}/revoke | Invalidates a certificate by adding it to a certificate revocation list.


# **approve**
> object approve(activation_code, body)

Marks the certificate signing request as approved. The host activation service will then continue with the signing process.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_provision

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
    api_instance = infra_provision.UICSRApi(api_client)
    activation_code = 'activation_code_example' # str | activation code is used by the clients to track the approval of the CSR
    body = infra_provision.ApproveCSRRequest() # ApproveCSRRequest | 

    try:
        # Marks the certificate signing request as approved. The host activation service will then continue with the signing process.
        api_response = api_instance.approve(activation_code, body)
        pprint("The response of UICSRApi->approve:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UICSRApi->approve: %s\n" % e)
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

# **deny**
> object deny(activation_code, body)

Marks the certificate signing request as denied.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_provision

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
    api_instance = infra_provision.UICSRApi(api_client)
    activation_code = 'activation_code_example' # str | activation code is used by the clients to track the approval of the CSR
    body = infra_provision.DenyCSRRequest() # DenyCSRRequest | 

    try:
        # Marks the certificate signing request as denied.
        api_response = api_instance.deny(activation_code, body)
        pprint("The response of UICSRApi->deny:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UICSRApi->deny: %s\n" % e)
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

# **list**
> ListCSRsResponse list(filter=filter, order_by=order_by, offset=offset, limit=limit, page_token=page_token, tfilter=tfilter, torder_by=torder_by)

User can list the certificate signing requests for an account.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_provision

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
    api_instance = infra_provision.UICSRApi(api_client)

    try:
        # User can list the certificate signing requests for an account.
        api_response = api_instance.list()
        pprint("The response of UICSRApi->list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UICSRApi->list: %s\n" % e)
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

# **revoke**
> object revoke(cert_serial, body)

Invalidates a certificate by adding it to a certificate revocation list.

The user can revoke the cert from the cloud (for example, if in case a host is compromised). Validation: - one of \"cert_serial\" or \"ophid\" should be provided - \"revoke_reason\" is optional

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_provision

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
    api_instance = infra_provision.UICSRApi(api_client)
    cert_serial = 'cert_serial_example' # str | x509 serial number of the certificate. This can be obtained by parsing the client certificate file on the onprem. Either cert_serial or ophid is required
    body = infra_provision.RevokeCertRequest() # RevokeCertRequest | 

    try:
        # Invalidates a certificate by adding it to a certificate revocation list.
        api_response = api_instance.revoke(cert_serial, body)
        pprint("The response of UICSRApi->revoke:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UICSRApi->revoke: %s\n" % e)
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

# **revoke2**
> object revoke2(ophid, body)

Invalidates a certificate by adding it to a certificate revocation list.

The user can revoke the cert from the cloud (for example, if in case a host is compromised). Validation: - one of \"cert_serial\" or \"ophid\" should be provided - \"revoke_reason\" is optional

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import infra_provision

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
    api_instance = infra_provision.UICSRApi(api_client)
    ophid = 'ophid_example' # str | On-prem host ID which can be obtained either from on-prem or NIOS-X UI portal(Manage > Infrastructure > Hosts > Select the onprem > click on 3 dots on top right side > General Information > Ophid) .
    body = infra_provision.RevokeCertRequest() # RevokeCertRequest | 

    try:
        # Invalidates a certificate by adding it to a certificate revocation list.
        api_response = api_instance.revoke2(ophid, body)
        pprint("The response of UICSRApi->revoke2:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UICSRApi->revoke2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ophid** | **str**| On-prem host ID which can be obtained either from on-prem or NIOS-X UI portal(Manage &gt; Infrastructure &gt; Hosts &gt; Select the onprem &gt; click on 3 dots on top right side &gt; General Information &gt; Ophid) . | 
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

