# Inheritance2InheritedUInt32

The inheritance configuration for a field of type _UInt32_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The inheritance setting for a field.  Valid values are: * _inherit_: Use the inherited value. * _override_: Use the value set in the object.  Defaults to _inherit_. | [optional] 
**display_name** | **str** | The human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | **int** | The inherited value. | [optional] [readonly] 

## Example

```python
from dns_config.models.inheritance2_inherited_u_int32 import Inheritance2InheritedUInt32

# TODO update the JSON string below
json = "{}"
# create an instance of Inheritance2InheritedUInt32 from a JSON string
inheritance2_inherited_u_int32_instance = Inheritance2InheritedUInt32.from_json(json)
# print the JSON string representation of the object
print(Inheritance2InheritedUInt32.to_json())

# convert the object into a dict
inheritance2_inherited_u_int32_dict = inheritance2_inherited_u_int32_instance.to_dict()
# create an instance of Inheritance2InheritedUInt32 from a dict
inheritance2_inherited_u_int32_from_dict = Inheritance2InheritedUInt32.from_dict(inheritance2_inherited_u_int32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


