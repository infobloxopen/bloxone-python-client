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
import dfp
from dfp.models.types_config_check_request import TypesConfigCheckRequest
from dfp.models.types_config_check_response import TypesConfigCheckResponse
from dfp.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://csp.infoblox.com/api/atcdfp/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dfp.Configuration(
    host = "https://csp.infoblox.com/api/atcdfp/v1"
)


# Enter a context with an instance of the API client
with dfp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dfp.AccountsApi(api_client)
    body = dfp.TypesConfigCheckRequest() # TypesConfigCheckRequest | 

    try:
        # Check Config.
        api_response = api_instance.check_config(body)
        print("The response of AccountsApi->check_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->check_config: %s\n" % e)
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

