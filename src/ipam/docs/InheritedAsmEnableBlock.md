# InheritedAsmEnableBlock

The inheritance block for ASM fields: _enable_, _enable_notification_, _reenable_date_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The inheritance setting.  Valid values are: * _inherit_: Use the inherited value. * _override_: Use the value set in the object.  Defaults to _inherit_. | [optional] 
**display_name** | **str** | The human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | [**AsmEnableBlock**](AsmEnableBlock.md) |  | [optional] 

## Example

```python
from ipam.models.inherited_asm_enable_block import InheritedAsmEnableBlock

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedAsmEnableBlock from a JSON string
inherited_asm_enable_block_instance = InheritedAsmEnableBlock.from_json(json)
# print the JSON string representation of the object
print(InheritedAsmEnableBlock.to_json())

# convert the object into a dict
inherited_asm_enable_block_dict = inherited_asm_enable_block_instance.to_dict()
# create an instance of InheritedAsmEnableBlock from a dict
inherited_asm_enable_block_from_dict = InheritedAsmEnableBlock.from_dict(inherited_asm_enable_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


