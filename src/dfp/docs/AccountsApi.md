# dfp.AccountsApi

All URIs are relative to *https://csp.infoblox.com/api/atcdfp/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_config**](AccountsApi.md#check_config) | **POST** /config/check | Check Config.


# **check_config**
> TypesConfigCheckResponse check_config(body)

Check Config.

Use this method to check configuration

### Example

```python
import os
from pprint import pprint

import dfp

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)


# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = dfp.AccountsApi(api_client)
    body = dfp.TypesConfigCheckRequest() # TypesConfigCheckRequest | 

    try:
        # Check Config.
        api_response = api_instance.check_config(body)
        pprint("The response of AccountsApi->check_config:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling AccountsApi->check_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TypesConfigCheckRequest**](TypesConfigCheckRequest.md)|  | 

### Return type

[**TypesConfigCheckResponse**](TypesConfigCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

