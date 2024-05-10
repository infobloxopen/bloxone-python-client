# ASMConfig

The __ASMConfig__ object represents Automated Scope Management configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asm_threshold** | **int** | ASM shows the number of addresses forecast to be used _forecast_period_ days in the future, if it is greater than _asm_threshold_ percent * _dhcp_total_ (see _dhcp_utilization_) then the subnet is flagged. | [optional] [default to 90]
**enable** | **bool** | Indicates if Automated Scope Management is enabled. | [optional] [default to True]
**enable_notification** | **bool** | Indicates if ASM should send notifications to the user. | [optional] [default to True]
**forecast_period** | **int** | The forecast period in days. | [optional] [default to 14]
**growth_factor** | **int** | Indicates the growth in the number or percentage of IP addresses. | [optional] [default to 20]
**growth_type** | **str** | The type of factor to use: _percent_ or _count_. | [optional] [default to 'percent']
**history** | **int** | The minimum amount of history needed before ASM can run on this subnet. | [optional] [default to 30]
**min_total** | **int** | The minimum size of range needed for ASM to run on this subnet. | [optional] [default to 10]
**min_unused** | **int** | The minimum percentage of addresses that must be available outside of the DHCP ranges and fixed addresses when making a suggested change.. | [optional] [default to 10]
**reenable_date** | **datetime** |  | [optional] 

## Example

```python
from ipam.models.asm_config import ASMConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ASMConfig from a JSON string
asm_config_instance = ASMConfig.from_json(json)
# print the JSON string representation of the object
print(ASMConfig.to_json())

# convert the object into a dict
asm_config_dict = asm_config_instance.to_dict()
# create an instance of ASMConfig from a dict
asm_config_from_dict = ASMConfig.from_dict(asm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


