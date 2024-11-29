# UpdateOverlappingBlockResponse

The response format to update the __OverlappingBlock__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OverlappingBlock**](OverlappingBlock.md) | The OverlappingBlock object. | [optional] 

## Example

```python
from ipam_federation.models.update_overlapping_block_response import UpdateOverlappingBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOverlappingBlockResponse from a JSON string
update_overlapping_block_response_instance = UpdateOverlappingBlockResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateOverlappingBlockResponse.to_json())

# convert the object into a dict
update_overlapping_block_response_dict = update_overlapping_block_response_instance.to_dict()
# create an instance of UpdateOverlappingBlockResponse from a dict
update_overlapping_block_response_from_dict = UpdateOverlappingBlockResponse.from_dict(update_overlapping_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


