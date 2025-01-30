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
import os
from pprint import pprint

import dns_config

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dns_config.CacheFlushApi(api_client)
    body = dns_config.CacheFlush() # CacheFlush | 

    try:
        # Create the Cache Flush object.
        api_response = api_instance.create(body)
        pprint("The response of CacheFlushApi->create:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling CacheFlushApi->create: %s\n" % e)
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

