# ListOverlappingBlockResponse

The response format to retrieve __OverlappingBlock__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[OverlappingBlock]**](OverlappingBlock.md) | A list of OverlappingBlock objects. | [optional] 

## Example

```python
from ipam_federation.models.list_overlapping_block_response import ListOverlappingBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOverlappingBlockResponse from a JSON string
list_overlapping_block_response_instance = ListOverlappingBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ListOverlappingBlockResponse.to_json())

# convert the object into a dict
list_overlapping_block_response_dict = list_overlapping_block_response_instance.to_dict()
# create an instance of ListOverlappingBlockResponse from a dict
list_overlapping_block_response_from_dict = ListOverlappingBlockResponse.from_dict(list_overlapping_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


