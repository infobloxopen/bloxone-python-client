# dns_config.ConvertDomainNameApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert**](ConvertDomainNameApi.md#convert) | **GET** /dns/convert_domain_name/{domain_name} | Convert the object.


# **convert**
> ConvertDomainNameResponse convert(domain_name)

Convert the object.

Use this method to convert between Internationalized Domain Name (IDN) and ASCII domain name (Punycode).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dns_config
from dns_config.models.convert_domain_name_response import ConvertDomainNameResponse
from dns_config.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dns_config.Configuration(
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
with dns_config.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dns_config.ConvertDomainNameApi(api_client)
    domain_name = 'domain_name_example' # str | Input domain name in either of IDN or punycode representations.

    try:
        # Convert the object.
        api_response = api_instance.convert(domain_name)
        print("The response of ConvertDomainNameApi->convert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertDomainNameApi->convert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Input domain name in either of IDN or punycode representations. | 

### Return type

[**ConvertDomainNameResponse**](ConvertDomainNameResponse.md)

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

