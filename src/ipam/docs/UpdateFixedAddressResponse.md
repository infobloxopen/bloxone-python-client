# UpdateFixedAddressResponse

The response format to update the __FixedAddress__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**FixedAddress**](FixedAddress.md) |  | [optional] 

## Example

```python
from ipam.models.update_fixed_address_response import UpdateFixedAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFixedAddressResponse from a JSON string
update_fixed_address_response_instance = UpdateFixedAddressResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateFixedAddressResponse.to_json())

# convert the object into a dict
update_fixed_address_response_dict = update_fixed_address_response_instance.to_dict()
# create an instance of UpdateFixedAddressResponse from a dict
update_fixed_address_response_from_dict = UpdateFixedAddressResponse.from_dict(update_fixed_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


