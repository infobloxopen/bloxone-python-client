# UpdateAddressBlockResponse

The response format to update the __AddressBlock__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**AddressBlock**](AddressBlock.md) |  | [optional] 

## Example

```python
from ipam.models.update_address_block_response import UpdateAddressBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAddressBlockResponse from a JSON string
update_address_block_response_instance = UpdateAddressBlockResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAddressBlockResponse.to_json())

# convert the object into a dict
update_address_block_response_dict = update_address_block_response_instance.to_dict()
# create an instance of UpdateAddressBlockResponse from a dict
update_address_block_response_from_dict = UpdateAddressBlockResponse.from_dict(update_address_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


