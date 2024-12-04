# ListNextAvailableOverlappingBlockResponse

The response format to list next available __OverlappingBlock__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[OverlappingBlock]**](OverlappingBlock.md) |  | [optional] 

## Example

```python
from ipam_federation.models.list_next_available_overlapping_block_response import ListNextAvailableOverlappingBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListNextAvailableOverlappingBlockResponse from a JSON string
list_next_available_overlapping_block_response_instance = ListNextAvailableOverlappingBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ListNextAvailableOverlappingBlockResponse.to_json())

# convert the object into a dict
list_next_available_overlapping_block_response_dict = list_next_available_overlapping_block_response_instance.to_dict()
# create an instance of ListNextAvailableOverlappingBlockResponse from a dict
list_next_available_overlapping_block_response_from_dict = ListNextAvailableOverlappingBlockResponse.from_dict(list_next_available_overlapping_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


