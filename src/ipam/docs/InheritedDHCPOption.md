# InheritedDHCPOption

The inheritance configuration for a field of type of _OptionItem_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The inheritance setting.  Valid values are: * _inherit_: Use the inherited value. * _block_: Don&#39;t use the inherited value.  Defaults to _inherit_. | [optional] 
**display_name** | **str** | The human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | [**InheritedDHCPOptionItem**](InheritedDHCPOptionItem.md) | The inherited value for the DHCP option. | [optional] [readonly] 

## Example

```python
from ipam.models.inherited_dhcp_option import InheritedDHCPOption

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedDHCPOption from a JSON string
inherited_dhcp_option_instance = InheritedDHCPOption.from_json(json)
# print the JSON string representation of the object
print(InheritedDHCPOption.to_json())

# convert the object into a dict
inherited_dhcp_option_dict = inherited_dhcp_option_instance.to_dict()
# create an instance of InheritedDHCPOption from a dict
inherited_dhcp_option_from_dict = InheritedDHCPOption.from_dict(inherited_dhcp_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


