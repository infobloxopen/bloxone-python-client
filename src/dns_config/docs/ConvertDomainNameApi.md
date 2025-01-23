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
import os
from pprint import pprint

import dns_config

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
    api_instance = dns_config.ConvertDomainNameApi(api_client)
    domain_name = 'domain_name_example' # str | Input domain name in either of IDN or punycode representations.

    try:
        # Convert the object.
        api_response = api_instance.convert(domain_name)
        pprint("The response of ConvertDomainNameApi->convert:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling ConvertDomainNameApi->convert: %s\n" % e)
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

