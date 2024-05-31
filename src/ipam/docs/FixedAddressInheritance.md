# FixedAddressInheritance

The __FixedAddressInheritance__ object specifies how and which fields _FixedAddress_ object inherits from the parent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_options** | [**InheritedDHCPOptionList**](InheritedDHCPOptionList.md) | The inheritance configuration for _dhcp_options_ field. | [optional] 
**header_option_filename** | [**InheritanceInheritedString**](InheritanceInheritedString.md) | The inheritance configuration for _header_option_filename_ field. | [optional] 
**header_option_server_address** | [**InheritanceInheritedString**](InheritanceInheritedString.md) | The inheritance configuration for _header_option_server_address_ field. | [optional] 
**header_option_server_name** | [**InheritanceInheritedString**](InheritanceInheritedString.md) | The inheritance configuration for _header_option_server_name_ field. | [optional] 

## Example

```python
from ipam.models.fixed_address_inheritance import FixedAddressInheritance

# TODO update the JSON string below
json = "{}"
# create an instance of FixedAddressInheritance from a JSON string
fixed_address_inheritance_instance = FixedAddressInheritance.from_json(json)
# print the JSON string representation of the object
print(FixedAddressInheritance.to_json())

# convert the object into a dict
fixed_address_inheritance_dict = fixed_address_inheritance_instance.to_dict()
# create an instance of FixedAddressInheritance from a dict
fixed_address_inheritance_from_dict = FixedAddressInheritance.from_dict(fixed_address_inheritance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


