# CreateFixedAddressResponse

The response format to create the __FixedAddress__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**FixedAddress**](FixedAddress.md) |  | [optional] 

## Example

```python
from ipam.models.create_fixed_address_response import CreateFixedAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFixedAddressResponse from a JSON string
create_fixed_address_response_instance = CreateFixedAddressResponse.from_json(json)
# print the JSON string representation of the object
print(CreateFixedAddressResponse.to_json())

# convert the object into a dict
create_fixed_address_response_dict = create_fixed_address_response_instance.to_dict()
# create an instance of CreateFixedAddressResponse from a dict
create_fixed_address_response_from_dict = CreateFixedAddressResponse.from_dict(create_fixed_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


