# CopyAddressBlockResponse

The response format to copy the __AddressBlock__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CopyResponse**](CopyResponse.md) |  | [optional] 

## Example

```python
from ipam.models.copy_address_block_response import CopyAddressBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CopyAddressBlockResponse from a JSON string
copy_address_block_response_instance = CopyAddressBlockResponse.from_json(json)
# print the JSON string representation of the object
print(CopyAddressBlockResponse.to_json())

# convert the object into a dict
copy_address_block_response_dict = copy_address_block_response_instance.to_dict()
# create an instance of CopyAddressBlockResponse from a dict
copy_address_block_response_from_dict = CopyAddressBlockResponse.from_dict(copy_address_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


