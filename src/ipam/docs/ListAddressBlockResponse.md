# ListAddressBlockResponse

The response format to retrieve __AddressBlock__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AddressBlock]**](AddressBlock.md) | A list of AddressBlock objects. | [optional] 

## Example

```python
from ipam.models.list_address_block_response import ListAddressBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAddressBlockResponse from a JSON string
list_address_block_response_instance = ListAddressBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ListAddressBlockResponse.to_json())

# convert the object into a dict
list_address_block_response_dict = list_address_block_response_instance.to_dict()
# create an instance of ListAddressBlockResponse from a dict
list_address_block_response_from_dict = ListAddressBlockResponse.from_dict(list_address_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


