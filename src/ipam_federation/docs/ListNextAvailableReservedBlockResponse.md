# ListNextAvailableReservedBlockResponse

The response format to list next available __ReservedBlock__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ReservedBlock]**](ReservedBlock.md) |  | [optional] 

## Example

```python
from ipam_federation.models.list_next_available_reserved_block_response import ListNextAvailableReservedBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListNextAvailableReservedBlockResponse from a JSON string
list_next_available_reserved_block_response_instance = ListNextAvailableReservedBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ListNextAvailableReservedBlockResponse.to_json())

# convert the object into a dict
list_next_available_reserved_block_response_dict = list_next_available_reserved_block_response_instance.to_dict()
# create an instance of ListNextAvailableReservedBlockResponse from a dict
list_next_available_reserved_block_response_from_dict = ListNextAvailableReservedBlockResponse.from_dict(list_next_available_reserved_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


