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
    api_instance = dns_config.ConvertRnameApi(api_client)
    email_address = 'email_address_example' # str | Input email address.

    try:
        # Convert the object.
        api_response = api_instance.convert_r_name(email_address)
        pprint("The response of ConvertRnameApi->convert_r_name:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling ConvertRnameApi->convert_r_name: %s\n" % e)
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

