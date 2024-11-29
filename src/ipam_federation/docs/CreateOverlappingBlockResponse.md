# CreateOverlappingBlockResponse

The response format to create the __OverlappingBlock__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OverlappingBlock**](OverlappingBlock.md) | The created OverlappingBlock object. | [optional] 

## Example

```python
from ipam_federation.models.create_overlapping_block_response import CreateOverlappingBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOverlappingBlockResponse from a JSON string
create_overlapping_block_response_instance = CreateOverlappingBlockResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOverlappingBlockResponse.to_json())

# convert the object into a dict
create_overlapping_block_response_dict = create_overlapping_block_response_instance.to_dict()
# create an instance of CreateOverlappingBlockResponse from a dict
create_overlapping_block_response_from_dict = CreateOverlappingBlockResponse.from_dict(create_overlapping_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


