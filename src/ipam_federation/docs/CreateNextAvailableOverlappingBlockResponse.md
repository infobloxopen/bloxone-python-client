# CreateNextAvailableOverlappingBlockResponse

The response format to allocate next available __OverlappingBlock__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[OverlappingBlock]**](OverlappingBlock.md) |  | [optional] 

## Example

```python
from ipam_federation.models.create_next_available_overlapping_block_response import CreateNextAvailableOverlappingBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNextAvailableOverlappingBlockResponse from a JSON string
create_next_available_overlapping_block_response_instance = CreateNextAvailableOverlappingBlockResponse.from_json(json)
# print the JSON string representation of the object
print(CreateNextAvailableOverlappingBlockResponse.to_json())

# convert the object into a dict
create_next_available_overlapping_block_response_dict = create_next_available_overlapping_block_response_instance.to_dict()
# create an instance of CreateNextAvailableOverlappingBlockResponse from a dict
create_next_available_overlapping_block_response_from_dict = CreateNextAvailableOverlappingBlockResponse.from_dict(create_next_available_overlapping_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


