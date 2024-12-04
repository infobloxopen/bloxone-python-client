# CreateReservedBlockResponse

The response format to create the __ReservedBlock__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ReservedBlock**](ReservedBlock.md) | The created ReservedBlock object. | [optional] 

## Example

```python
from ipam_federation.models.create_reserved_block_response import CreateReservedBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReservedBlockResponse from a JSON string
create_reserved_block_response_instance = CreateReservedBlockResponse.from_json(json)
# print the JSON string representation of the object
print(CreateReservedBlockResponse.to_json())

# convert the object into a dict
create_reserved_block_response_dict = create_reserved_block_response_instance.to_dict()
# create an instance of CreateReservedBlockResponse from a dict
create_reserved_block_response_from_dict = CreateReservedBlockResponse.from_dict(create_reserved_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


