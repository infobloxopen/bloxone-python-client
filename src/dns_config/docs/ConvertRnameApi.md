# dns_config.ConvertRnameApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_r_name**](ConvertRnameApi.md#convert_r_name) | **GET** /dns/convert_rname/{email_address} | Convert the object.


# **convert_r_name**
> ConvertRNameResponse convert_r_name(email_address)

Convert the object.

Use this method to convert email address to the master file RNAME format.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dns_config
from dns_config.models.convert_r_name_response import ConvertRNameResponse
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
    api_instance = dns_config.ConvertRnameApi(api_client)
    email_address = 'email_address_example' # str | Input email address.

    try:
        # Convert the object.
        api_response = api_instance.convert_r_name(email_address)
        print("The response of ConvertRnameApi->convert_r_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConvertRnameApi->convert_r_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | **str**| Input email address. | 

### Return type

[**ConvertRNameResponse**](ConvertRNameResponse.md)

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

