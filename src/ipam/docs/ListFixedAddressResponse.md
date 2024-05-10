# ListFixedAddressResponse

The response format to retrieve __FixedAddress__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[FixedAddress]**](FixedAddress.md) | The list of FixedAddress objects. | [optional] 

## Example

```python
from ipam.models.list_fixed_address_response import ListFixedAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListFixedAddressResponse from a JSON string
list_fixed_address_response_instance = ListFixedAddressResponse.from_json(json)
# print the JSON string representation of the object
print(ListFixedAddressResponse.to_json())

# convert the object into a dict
list_fixed_address_response_dict = list_fixed_address_response_instance.to_dict()
# create an instance of ListFixedAddressResponse from a dict
list_fixed_address_response_from_dict = ListFixedAddressResponse.from_dict(list_fixed_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


