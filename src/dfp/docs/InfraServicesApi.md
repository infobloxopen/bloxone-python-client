# dfp.InfraServicesApi

All URIs are relative to *https://csp.infoblox.com/api/atcdfp/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_dfp_service**](InfraServicesApi.md#create_or_update_dfp_service) | **PUT** /dfp_services/{payload.service_id} | Update DNS Forwarding Proxy services.
[**list_dfp_services**](InfraServicesApi.md#list_dfp_services) | **GET** /dfp_services | List DNS Forwarding Proxy services.
[**read_dfp_service**](InfraServicesApi.md#read_dfp_service) | **GET** /dfp_services/{service_id} | Read DNS Forwarding Proxy services.


# **create_or_update_dfp_service**
> DfpCreateOrUpdateResponse create_or_update_dfp_service(payload_service_id, body)

Update DNS Forwarding Proxy services.

Use this method to update resolvers for the specified DNS Forwarding Proxy Service. 

### Example

```python
import os
from pprint import pprint

import dfp

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = dfp.InfraServicesApi(api_client)
    payload_service_id = 'payload_service_id_example' # str | The DNS Forwarding Proxy Service ID object identifier.
    body = dfp.DfpCreateOrUpdatePayload() # DfpCreateOrUpdatePayload | The DNS Forwarding Proxy object.

    try:
        # Update DNS Forwarding Proxy services.
        api_response = api_instance.create_or_update_dfp_service(payload_service_id, body)
        pprint("The response of InfraServicesApi->create_or_update_dfp_service:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling InfraServicesApi->create_or_update_dfp_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload_service_id** | **str**| The DNS Forwarding Proxy Service ID object identifier. | 
 **body** | [**DfpCreateOrUpdatePayload**](DfpCreateOrUpdatePayload.md)| The DNS Forwarding Proxy object. | 

### Return type

[**DfpCreateOrUpdateResponse**](DfpCreateOrUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PUT operation response |  -  |
**400** |  - &#39;id&#39; value must be greater than or equal to zero |  -  |
**404** |  - &#39;id&#39; value must contain existing DFP identifier |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfp_services**
> DfpListResponse list_dfp_services(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token)

List DNS Forwarding Proxy services.

Use this method to retrieve information on all DNS Forwarding Proxy services.  

### Example

```python
import os
from pprint import pprint

import dfp

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = dfp.InfraServicesApi(api_client)

    try:
        # List DNS Forwarding Proxy services.
        api_response = api_instance.list_dfp_services()
        pprint("The response of InfraServicesApi->list_dfp_services:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling InfraServicesApi->list_dfp_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;.  You can filter by following fields:  | Name                    | type     | Supported Op                | | ----------------------- | -------- | --------------------------- | | service_name            | string   | !&#x3D;, &#x3D;&#x3D;, ~, !~, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D; | | internal_domain_lists   | [int32]  | !&#x3D;, &#x3D;&#x3D;, ~, !~, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D; | | policy_id               | int32    | !&#x3D;, &#x3D;&#x3D;, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D;        | | default_security_policy | bool     | !&#x3D;, &#x3D;&#x3D;                      |   In addition groupping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Groupping Operators  |  Example: &#x60;&#x60;&#x60; ?_filter&#x3D;\&quot;((service_name&#x3D;&#x3D;&#39;dfp1&#39;)or(policy_id~&#39;oph&#39;))and(default_security_policy!&#x3D;&#39;true&#39;)\&quot; &#x60;&#x60;&#x60;  | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 

### Return type

[**DfpListResponse**](DfpListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_dfp_service**
> DfpReadResponse read_dfp_service(service_id, id=id, fields=fields, name=name)

Read DNS Forwarding Proxy services.

Use this method to retrieve information on the specified DNS Forwarding Proxy service. 

### Example

```python
import os
from pprint import pprint

import dfp

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('UNIVERSAL_DDI_CSP_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = dfp.InfraServicesApi(api_client)
    service_id = 'service_id_example' # str | The On-Prem Application Service identifier. For internal Use only

    try:
        # Read DNS Forwarding Proxy services.
        api_response = api_instance.read_dfp_service(service_id)
        pprint("The response of InfraServicesApi->read_dfp_service:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling InfraServicesApi->read_dfp_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The On-Prem Application Service identifier. For internal Use only | 
 **id** | **int**| The DNS Forwarding Proxy object identifier. | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **name** | **str**| The name of the DNS Forwarding Proxy. Used only if the &#39;id&#39; field is empty. | [optional] 

### Return type

[**DfpReadResponse**](DfpReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |
**404** |  - &#39;id&#39; value must contain existing DFP identifier |  -  |
**500** |  - Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

