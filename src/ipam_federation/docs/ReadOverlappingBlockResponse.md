# ReadOverlappingBlockResponse

The response format to retrieve the __OverlappingBlock__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OverlappingBlock**](OverlappingBlock.md) | The OverlappingBlock object. | [optional] 

## Example

```python
from ipam_federation.models.read_overlapping_block_response import ReadOverlappingBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadOverlappingBlockResponse from a JSON string
read_overlapping_block_response_instance = ReadOverlappingBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ReadOverlappingBlockResponse.to_json())

# convert the object into a dict
read_overlapping_block_response_dict = read_overlapping_block_response_instance.to_dict()
# create an instance of ReadOverlappingBlockResponse from a dict
read_overlapping_block_response_from_dict = ReadOverlappingBlockResponse.from_dict(read_overlapping_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


