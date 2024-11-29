# ipam_federation.NextAvailableReservedBlockApi

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_next_available_reserved_blocks**](NextAvailableReservedBlockApi.md#list_next_available_reserved_blocks) | **GET** /federation/federated_block/{id}/next_available_reserved_block | List the next available reserved block.


# **list_next_available_reserved_blocks**
> ListNextAvailableReservedBlockResponse list_next_available_reserved_blocks(id, cidr=cidr, count=count, name=name, comment=comment)

List the next available reserved block.

Use this method to list the next \"n\" available __ReservedBlock__ object with user specified predicates. The response will be \"n\" __ReservedBlock__ objects.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import ipam_federation

from bloxone_client.api_client import ApiClient
from bloxone_client.configuration import Configuration

# Configure CSP URL and API key for authorization via environment variables
config = Configuration(
    csp_url = os.getenv('BLOXONE_CSP_URL', "https://csp.infoblox.com"),
    api_key = os.getenv('BLOXONE_API_KEY', ""),
)

# Enter a context with an instance of the API client
with ApiClient(config) as api_client:
    # Create an instance of the API class
    api_instance = ipam_federation.NextAvailableReservedBlockApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    cidr = 56 # int | The CIDR of the federated block. This is required, if _address_ does not specify it in its input. (optional)
    count = 56 # int | The count of __Block__ required. If not provided, it will default to 1. (optional)
    name = 'name_example' # str | The name to be provided. (optional)
    comment = 'comment_example' # str | The description for the _federation/federated_block_. May contain 0 to 1024 characters. Can include UTF-8. (optional)

    try:
        # List the next available reserved block.
        api_response = api_instance.list_next_available_reserved_blocks(id, cidr=cidr, count=count, name=name, comment=comment)
        print("The response of NextAvailableReservedBlockApi->list_next_available_reserved_blocks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NextAvailableReservedBlockApi->list_next_available_reserved_blocks: %s\n" % e)
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

[**ListNextAvailableReservedBlockResponse**](ListNextAvailableReservedBlockResponse.md)

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

