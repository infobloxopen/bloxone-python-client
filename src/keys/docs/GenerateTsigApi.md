# keys.GenerateTsigApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_tsig**](GenerateTsigApi.md#generate_tsig) | **GET** /keys/generate_tsig | Generate TSIG key with a random secret.


# **generate_tsig**
> GenerateTSIGResponse generate_tsig(algorithm=algorithm)

Generate TSIG key with a random secret.

Use this method to generate a TSIG key with a random secret using the specified algorithm.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import keys

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = keys.GenerateTsigApi(api_client)

    try:
        # Generate TSIG key with a random secret.
        api_response = api_instance.generate_tsig()
        pprint("The response of GenerateTsigApi->generate_tsig:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling GenerateTsigApi->generate_tsig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algorithm** | **str**| The TSIG key algorithm.  Valid values are: * _hmac_sha256_ * _hmac_sha1_ * _hmac_sha224_ * _hmac_sha384_ * _hmac_sha512_  Defaults to _hmac_sha256_. | [optional] 

### Return type

[**GenerateTSIGResponse**](GenerateTSIGResponse.md)

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

