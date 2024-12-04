# ipam_federation.NextAvailableOverlappingBlockApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_next_available_overlapping_blocks**](NextAvailableOverlappingBlockApi.md#list_next_available_overlapping_blocks) | **GET** /federation/federated_block/{id}/next_available_overlapping_block | List the next available overlapping block.


# **list_next_available_overlapping_blocks**
> ListNextAvailableOverlappingBlockResponse list_next_available_overlapping_blocks(id, cidr=cidr, count=count, name=name, comment=comment)

List the next available overlapping block.

Use this method to list the next \"n\" available __OverlappingBlock__ object with user specified predicates. The response will be \"n\" __OverlappingBlock__ objects.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam_federation

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Defining the CSP URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure API key authorization: ApiKeyAuth
configuration.api_key = os.getenv("BLOXONE_API_KEY")

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = ipam_federation.NextAvailableOverlappingBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    cidr = 56 # int | The CIDR of the federated block. This is required, if _address_ does not specify it in its input. (optional)
    count = 56 # int | The count of __Block__ required. If not provided, it will default to 1. (optional)
    name = 'name_example' # str | The name to be provided. (optional)
    comment = 'comment_example' # str | The description for the _federation/federated_block_. May contain 0 to 1024 characters. Can include UTF-8. (optional)

    try:
        # List the next available overlapping block.
        api_response = api_instance.list_next_available_overlapping_blocks(id, cidr=cidr, count=count, name=name, comment=comment)
        pprint("The response of NextAvailableOverlappingBlockApi->list_next_available_overlapping_blocks:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling NextAvailableOverlappingBlockApi->list_next_available_overlapping_blocks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **cidr** | **int**| The CIDR of the federated block. This is required, if _address_ does not specify it in its input. | [optional] 
 **count** | **int**| The count of __Block__ required. If not provided, it will default to 1. | [optional] 
 **name** | **str**| The name to be provided. | [optional] 
 **comment** | **str**| The description for the _federation/federated_block_. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 

### Return type

[**ListNextAvailableOverlappingBlockResponse**](ListNextAvailableOverlappingBlockResponse.md)

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

