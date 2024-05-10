# InheritedDHCPOptionItem

A wrapper of item (_dhcp/option_item_) in a list of Inherited DHCP options. It contains extra fields not covered by OptionItem.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | [**OptionItem**](OptionItem.md) |  | [optional] 
**overriding_group** | **str** | The resource identifier. | [optional] 

## Example

```python
from ipam.models.inherited_dhcp_option_item import InheritedDHCPOptionItem

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedDHCPOptionItem from a JSON string
inherited_dhcp_option_item_instance = InheritedDHCPOptionItem.from_json(json)
# print the JSON string representation of the object
print(InheritedDHCPOptionItem.to_json())

# convert the object into a dict
inherited_dhcp_option_item_dict = inherited_dhcp_option_item_instance.to_dict()
# create an instance of InheritedDHCPOptionItem from a dict
inherited_dhcp_option_item_from_dict = InheritedDHCPOptionItem.from_dict(inherited_dhcp_option_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


