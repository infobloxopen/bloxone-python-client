# InheritanceInheritedIdentifier

The inheritance configuration for a field of type _Identifier_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The inheritance setting for a field.  Valid values are: * _inherit_: Use the inherited value. * _override_: Use the value set in the object.  Defaults to _inherit_. | [optional] 
**display_name** | **str** | The human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | **str** | The resource identifier. | [optional] 

## Example

```python
from ipam.models.inheritance_inherited_identifier import InheritanceInheritedIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of InheritanceInheritedIdentifier from a JSON string
inheritance_inherited_identifier_instance = InheritanceInheritedIdentifier.from_json(json)
# print the JSON string representation of the object
print(InheritanceInheritedIdentifier.to_json())

# convert the object into a dict
inheritance_inherited_identifier_dict = inheritance_inherited_identifier_instance.to_dict()
# create an instance of InheritanceInheritedIdentifier from a dict
inheritance_inherited_identifier_from_dict = InheritanceInheritedIdentifier.from_dict(inheritance_inherited_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


