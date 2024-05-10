# ReadAddressBlockResponse

The response format to retrieve the __AddressBlock__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**AddressBlock**](AddressBlock.md) |  | [optional] 

## Example

```python
from ipam.models.read_address_block_response import ReadAddressBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadAddressBlockResponse from a JSON string
read_address_block_response_instance = ReadAddressBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ReadAddressBlockResponse.to_json())

# convert the object into a dict
read_address_block_response_dict = read_address_block_response_instance.to_dict()
# create an instance of ReadAddressBlockResponse from a dict
read_address_block_response_from_dict = ReadAddressBlockResponse.from_dict(read_address_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


