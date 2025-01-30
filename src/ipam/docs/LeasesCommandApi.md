# ipam.LeasesCommandApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](LeasesCommandApi.md#create) | **POST** /dhcp/leases_command | Perform actions like clearing DHCP lease(s).


# **create**
> CreateLeasesCommandResponse create(body)

Perform actions like clearing DHCP lease(s).

Use this method to create a __LeasesCommand__ object. The __LeasesCommand__ object (_dhcp/leases_command_) is used for performing an action like clearing DHCP lease(s).

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.api_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = ipam.LeasesCommandApi(api_client)
    body = ipam.LeasesCommand() # LeasesCommand | 

    try:
        # Perform actions like clearing DHCP lease(s).
        api_response = api_instance.create(body)
        pprint("The response of LeasesCommandApi->create:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling LeasesCommandApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeasesCommand**](LeasesCommand.md)|  | 

### Return type

[**CreateLeasesCommandResponse**](CreateLeasesCommandResponse.md)

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

