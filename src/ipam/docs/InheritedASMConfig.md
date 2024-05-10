# InheritedASMConfig

The inheritance configuration for the __ASMConfig__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asm_enable_block** | [**InheritedAsmEnableBlock**](InheritedAsmEnableBlock.md) |  | [optional] 
**asm_growth_block** | [**InheritedAsmGrowthBlock**](InheritedAsmGrowthBlock.md) |  | [optional] 
**asm_threshold** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) |  | [optional] 
**forecast_period** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) |  | [optional] 
**history** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) |  | [optional] 
**min_total** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) |  | [optional] 
**min_unused** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) |  | [optional] 

## Example

```python
from ipam.models.inherited_asm_config import InheritedASMConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedASMConfig from a JSON string
inherited_asm_config_instance = InheritedASMConfig.from_json(json)
# print the JSON string representation of the object
print(InheritedASMConfig.to_json())

# convert the object into a dict
inherited_asm_config_dict = inherited_asm_config_instance.to_dict()
# create an instance of InheritedASMConfig from a dict
inherited_asm_config_from_dict = InheritedASMConfig.from_dict(inherited_asm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


