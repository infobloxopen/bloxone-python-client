# redirect.CertificateApi

All URIs are relative to *https://csp.infoblox.com/api/atcfw/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_proxy_certificates**](CertificateApi.md#get_proxy_certificates) | **GET** /cert_download_urls | Get Proxy Certificates


# **get_proxy_certificates**
> ProxyCertResponse get_proxy_certificates(fields=fields)

Get Proxy Certificates

Use this method to get certificates to use proxy server 

### Example


```python
import redirect
from redirect.models.proxy_cert_response import ProxyCertResponse
from redirect.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcfw/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = redirect.Configuration(
    host = "https://csp.infoblox.com/api/atcfw/v1"
)


# Enter a context with an instance of the API client
with redirect.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = redirect.CertificateApi(api_client)
    fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

    try:
        # Get Proxy Certificates
        api_response = api_instance.get_proxy_certificates(fields=fields)
        print("The response of CertificateApi->get_proxy_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateApi->get_proxy_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**ProxyCertResponse**](ProxyCertResponse.md)

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

