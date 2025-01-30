# keys.UploadApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload**](UploadApi.md#upload) | **POST** /keys/upload | Upload content to the keys service.


# **upload**
> DdiuploadResponse upload(body)

Upload content to the keys service.

Use this method to upload specified content type to the keys service.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import keys

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
    api_instance = keys.UploadApi(api_client)
    body = keys.UploadRequest() # UploadRequest | 

    try:
        # Upload content to the keys service.
        api_response = api_instance.upload(body)
        pprint("The response of UploadApi->upload:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling UploadApi->upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UploadRequest**](UploadRequest.md)|  | 

### Return type

[**DdiuploadResponse**](DdiuploadResponse.md)

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

