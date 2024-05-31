# DHCPOptionsInheritance

The inheritance configuration that specifies how the _dhcp_options_ field is inherited from the parent object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_options** | [**InheritedDHCPOptionList**](InheritedDHCPOptionList.md) | The inheritance configuration for the _dhcp_options_ field. | [optional] 

## Example

```python
from ipam.models.dhcp_options_inheritance import DHCPOptionsInheritance

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPOptionsInheritance from a JSON string
dhcp_options_inheritance_instance = DHCPOptionsInheritance.from_json(json)
# print the JSON string representation of the object
print(DHCPOptionsInheritance.to_json())

# convert the object into a dict
dhcp_options_inheritance_dict = dhcp_options_inheritance_instance.to_dict()
# create an instance of DHCPOptionsInheritance from a dict
dhcp_options_inheritance_from_dict = DHCPOptionsInheritance.from_dict(dhcp_options_inheritance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


