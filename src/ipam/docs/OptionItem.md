# OptionItem

An item (_dhcp/option_item_) in a list of DHCP options. May be either a specific option or a group of options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | The resource identifier. | [optional] 
**option_code** | **str** | The resource identifier. | [optional] 
**option_value** | **str** | The option value. | [optional] 
**type** | **str** | The type of item.  Valid values are: * _group_ * _option_ | [optional] 

## Example

```python
from ipam.models.option_item import OptionItem

# TODO update the JSON string below
json = "{}"
# create an instance of OptionItem from a JSON string
option_item_instance = OptionItem.from_json(json)
# print the JSON string representation of the object
print(OptionItem.to_json())

# convert the object into a dict
option_item_dict = option_item_instance.to_dict()
# create an instance of OptionItem from a dict
option_item_from_dict = OptionItem.from_dict(option_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


