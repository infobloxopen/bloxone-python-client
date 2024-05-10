# OptionGroup

An __OptionGroup__ object (_dhcp/option_group_) is a named collection of options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The description for the option group. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**dhcp_options** | [**List[OptionItem]**](OptionItem.md) | The list of DHCP options for the option group. May be either a specific option or a group of options. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The name of the option group. Must contain 1 to 256 characters. Can include UTF-8. | 
**protocol** | **str** | The type of protocol (_ip4_ or _ip6_). | [optional] 
**tags** | **object** | The tags for the option group in JSON format. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 

## Example

```python
from ipam.models.option_group import OptionGroup

# TODO update the JSON string below
json = "{}"
# create an instance of OptionGroup from a JSON string
option_group_instance = OptionGroup.from_json(json)
# print the JSON string representation of the object
print(OptionGroup.to_json())

# convert the object into a dict
option_group_dict = option_group_instance.to_dict()
# create an instance of OptionGroup from a dict
option_group_from_dict = OptionGroup.from_dict(option_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


