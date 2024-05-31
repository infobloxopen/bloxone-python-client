# InheritedASMConfig

The inheritance configuration for the __ASMConfig__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asm_enable_block** | [**InheritedAsmEnableBlock**](InheritedAsmEnableBlock.md) | The block of ASM fields: _enable_, _enable_notification_, _reenable_date_. | [optional] 
**asm_growth_block** | [**InheritedAsmGrowthBlock**](InheritedAsmGrowthBlock.md) | The block of ASM fields: _growth_factor_, _growth_type_. | [optional] 
**asm_threshold** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) | ASM shows the number of addresses forecast to be used _forecast_period_ days in the future, if it is greater than _asm_threshold_percent_ * _dhcp_total_ (see _dhcp_utilization_) then the subnet is flagged. | [optional] 
**forecast_period** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) | The forecast period in days. | [optional] 
**history** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) | The minimum amount of history needed before ASM can run on this subnet. | [optional] 
**min_total** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) | The minimum size of range needed for ASM to run on this subnet. | [optional] 
**min_unused** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) | The minimum percentage of addresses that must be available outside of the DHCP ranges and fixed addresses when making a suggested change. | [optional] 

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


