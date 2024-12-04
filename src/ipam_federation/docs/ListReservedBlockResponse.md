# ListReservedBlockResponse

The response format to retrieve __ReservedBlock__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ReservedBlock]**](ReservedBlock.md) | A list of ReservedBlock objects. | [optional] 

## Example

```python
from ipam_federation.models.list_reserved_block_response import ListReservedBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListReservedBlockResponse from a JSON string
list_reserved_block_response_instance = ListReservedBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ListReservedBlockResponse.to_json())

# convert the object into a dict
list_reserved_block_response_dict = list_reserved_block_response_instance.to_dict()
# create an instance of ListReservedBlockResponse from a dict
list_reserved_block_response_from_dict = ListReservedBlockResponse.from_dict(list_reserved_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


