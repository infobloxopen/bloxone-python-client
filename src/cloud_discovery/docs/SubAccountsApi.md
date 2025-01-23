# cloud_discovery.SubAccountsApi

All URIs are relative to *http://csp.infoblox.com/api/cloud_discovery/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](SubAccountsApi.md#list) | **POST** /sub_accounts | List Sub-accounts


# **list**
> SubAccountListResponseV2 list(body)

List Sub-accounts

Use this method to list Sub-accounts

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import cloud_discovery

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
    api_instance = cloud_discovery.SubAccountsApi(api_client)
    body = cloud_discovery.SubAccountListRequestV2() # SubAccountListRequestV2 | 

    try:
        # List Sub-accounts
        api_response = api_instance.list(body)
        pprint("The response of SubAccountsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling SubAccountsApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubAccountListRequestV2**](SubAccountListRequestV2.md)|  | 

### Return type

[**SubAccountListResponseV2**](SubAccountListResponseV2.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | POST operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

