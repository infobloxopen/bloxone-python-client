# InheritanceInheritedBool

The inheritance configuration for a field of type _Bool_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The inheritance setting for a field.  Valid values are: * _inherit_: Use the inherited value. * _override_: Use the value set in the object.  Defaults to _inherit_. | [optional] 
**display_name** | **str** | The human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | **bool** | The inherited value. | [optional] [readonly] 

## Example

```python
from ipam.models.inheritance_inherited_bool import InheritanceInheritedBool

# TODO update the JSON string below
json = "{}"
# create an instance of InheritanceInheritedBool from a JSON string
inheritance_inherited_bool_instance = InheritanceInheritedBool.from_json(json)
# print the JSON string representation of the object
print(InheritanceInheritedBool.to_json())

# convert the object into a dict
inheritance_inherited_bool_dict = inheritance_inherited_bool_instance.to_dict()
# create an instance of InheritanceInheritedBool from a dict
inheritance_inherited_bool_from_dict = InheritanceInheritedBool.from_dict(inheritance_inherited_bool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


