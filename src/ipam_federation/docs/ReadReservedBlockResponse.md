# ReadReservedBlockResponse

The response format to retrieve the __ReservedBlock__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ReservedBlock**](ReservedBlock.md) | The ReservedBlock object. | [optional] 

## Example

```python
from ipam_federation.models.read_reserved_block_response import ReadReservedBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadReservedBlockResponse from a JSON string
read_reserved_block_response_instance = ReadReservedBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ReadReservedBlockResponse.to_json())

# convert the object into a dict
read_reserved_block_response_dict = read_reserved_block_response_instance.to_dict()
# create an instance of ReadReservedBlockResponse from a dict
read_reserved_block_response_from_dict = ReadReservedBlockResponse.from_dict(read_reserved_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


