# InheritedDHCPOptionList

The inheritance configuration for a field that contains list of _OptionItem_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The inheritance setting.  Valid values are: * _inherit_: Use the inherited value. * _block_: Don&#39;t use the inherited value.  Defaults to _inherit_. | [optional] 
**value** | [**List[InheritedDHCPOption]**](InheritedDHCPOption.md) | The inherited DHCP option values. | [optional] 

## Example

```python
from ipam.models.inherited_dhcp_option_list import InheritedDHCPOptionList

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedDHCPOptionList from a JSON string
inherited_dhcp_option_list_instance = InheritedDHCPOptionList.from_json(json)
# print the JSON string representation of the object
print(InheritedDHCPOptionList.to_json())

# convert the object into a dict
inherited_dhcp_option_list_dict = inherited_dhcp_option_list_instance.to_dict()
# create an instance of InheritedDHCPOptionList from a dict
inherited_dhcp_option_list_from_dict = InheritedDHCPOptionList.from_dict(inherited_dhcp_option_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


