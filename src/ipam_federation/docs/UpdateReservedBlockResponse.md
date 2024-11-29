# UpdateReservedBlockResponse

The response format to update the __ReservedBlock__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ReservedBlock**](ReservedBlock.md) | The ReservedBlock object. | [optional] 

## Example

```python
from ipam_federation.models.update_reserved_block_response import UpdateReservedBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReservedBlockResponse from a JSON string
update_reserved_block_response_instance = UpdateReservedBlockResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateReservedBlockResponse.to_json())

# convert the object into a dict
update_reserved_block_response_dict = update_reserved_block_response_instance.to_dict()
# create an instance of UpdateReservedBlockResponse from a dict
update_reserved_block_response_from_dict = UpdateReservedBlockResponse.from_dict(update_reserved_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


