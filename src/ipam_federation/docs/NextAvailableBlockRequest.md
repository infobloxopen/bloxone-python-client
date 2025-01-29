# NextAvailableBlockRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **int** | The CIDR of the federated block. This is required, if _address_ does not specify it in its input. | [optional] 
**comment** | **str** | The description for the _federation/federated_block_. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**count** | **int** | The count of __Block__ required. If not provided, it will default to 1. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The name to be provided. | [optional] 
**tags** | **object** | The tags for the federated block in JSON format. | [optional] 

## Example

```python
from ipam_federation.models.next_available_block_request import NextAvailableBlockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NextAvailableBlockRequest from a JSON string
next_available_block_request_instance = NextAvailableBlockRequest.from_json(json)
# print the JSON string representation of the object
print(NextAvailableBlockRequest.to_json())

# convert the object into a dict
next_available_block_request_dict = next_available_block_request_instance.to_dict()
# create an instance of NextAvailableBlockRequest from a dict
next_available_block_request_from_dict = NextAvailableBlockRequest.from_dict(next_available_block_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


