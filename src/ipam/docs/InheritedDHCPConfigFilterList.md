# InheritedDHCPConfigFilterList

The inheritance configuration for a field of type list of identifier that represent list of filter attached to _DHCPConfig_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The inheritance setting.  Valid values are: * _inherit_: Use the inherited value. * _override_: Use the value set in the object.  Defaults to _inherit_. | [optional] 
**display_name** | **str** | The human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | **List[str]** | The resource identifier. | [optional] 

## Example

```python
from ipam.models.inherited_dhcp_config_filter_list import InheritedDHCPConfigFilterList

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedDHCPConfigFilterList from a JSON string
inherited_dhcp_config_filter_list_instance = InheritedDHCPConfigFilterList.from_json(json)
# print the JSON string representation of the object
print(InheritedDHCPConfigFilterList.to_json())

# convert the object into a dict
inherited_dhcp_config_filter_list_dict = inherited_dhcp_config_filter_list_instance.to_dict()
# create an instance of InheritedDHCPConfigFilterList from a dict
inherited_dhcp_config_filter_list_from_dict = InheritedDHCPConfigFilterList.from_dict(inherited_dhcp_config_filter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


