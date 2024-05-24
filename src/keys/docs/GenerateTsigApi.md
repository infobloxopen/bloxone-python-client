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
import keys
from keys.models.generate_tsig_response import GenerateTSIGResponse
from keys.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = keys.Configuration(
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
with keys.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = keys.GenerateTsigApi(api_client)
    algorithm = 'algorithm_example' # str | The TSIG key algorithm.  Valid values are: * _hmac_sha256_ * _hmac_sha1_ * _hmac_sha224_ * _hmac_sha384_ * _hmac_sha512_  Defaults to _hmac_sha256_. (optional)

    try:
        # Generate TSIG key with a random secret.
        api_response = api_instance.generate_tsig(algorithm=algorithm)
        print("The response of GenerateTsigApi->generate_tsig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerateTsigApi->generate_tsig: %s\n" % e)
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

