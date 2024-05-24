# dns_config.CacheFlushApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CacheFlushApi.md#create) | **POST** /dns/cache_flush | Create the Cache Flush object.


# **create**
> object create(body)

Create the Cache Flush object.

Use this method to create a Cache Flush object. The Cache Flush object is for removing entries from the DNS cache on a host. The host must be available and running DNS for this to succeed.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import dns_config
from dns_config.models.cache_flush import CacheFlush
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
    api_instance = dns_config.CacheFlushApi(api_client)
    body = dns_config.CacheFlush() # CacheFlush | 

    try:
        # Create the Cache Flush object.
        api_response = api_instance.create(body)
        print("The response of CacheFlushApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheFlushApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CacheFlush**](CacheFlush.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | POST operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

