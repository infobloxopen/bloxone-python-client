# CreateAddressBlockResponse

The response format to create the __AddressBlock__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**AddressBlock**](AddressBlock.md) | The created AddressBlock object. | [optional] 

## Example

```python
from ipam.models.create_address_block_response import CreateAddressBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAddressBlockResponse from a JSON string
create_address_block_response_instance = CreateAddressBlockResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAddressBlockResponse.to_json())

# convert the object into a dict
create_address_block_response_dict = create_address_block_response_instance.to_dict()
# create an instance of CreateAddressBlockResponse from a dict
create_address_block_response_from_dict = CreateAddressBlockResponse.from_dict(create_address_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


