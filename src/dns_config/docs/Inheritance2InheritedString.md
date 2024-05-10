# Inheritance2InheritedString

The inheritance configuration for a field of type _String_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The inheritance setting for a field.  Valid values are: * _inherit_: Use the inherited value. * _override_: Use the value set in the object.  Defaults to _inherit_. | [optional] 
**display_name** | **str** | The human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | **str** | The inherited value. | [optional] [readonly] 

## Example

```python
from dns_config.models.inheritance2_inherited_string import Inheritance2InheritedString

# TODO update the JSON string below
json = "{}"
# create an instance of Inheritance2InheritedString from a JSON string
inheritance2_inherited_string_instance = Inheritance2InheritedString.from_json(json)
# print the JSON string representation of the object
print(Inheritance2InheritedString.to_json())

# convert the object into a dict
inheritance2_inherited_string_dict = inheritance2_inherited_string_instance.to_dict()
# create an instance of Inheritance2InheritedString from a dict
inheritance2_inherited_string_from_dict = Inheritance2InheritedString.from_dict(inheritance2_inherited_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


