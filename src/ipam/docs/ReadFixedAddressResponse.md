# ReadFixedAddressResponse

The response format to retrieve the __FixedAddress__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**FixedAddress**](FixedAddress.md) |  | [optional] 

## Example

```python
from ipam.models.read_fixed_address_response import ReadFixedAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadFixedAddressResponse from a JSON string
read_fixed_address_response_instance = ReadFixedAddressResponse.from_json(json)
# print the JSON string representation of the object
print(ReadFixedAddressResponse.to_json())

# convert the object into a dict
read_fixed_address_response_dict = read_fixed_address_response_instance.to_dict()
# create an instance of ReadFixedAddressResponse from a dict
read_fixed_address_response_from_dict = ReadFixedAddressResponse.from_dict(read_fixed_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


