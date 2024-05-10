# ASM

The __ASM__ object is a synthetic object representing the suggestions from the Automated Scope Management suggestion engine for expanding subnet or range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**back_end** | **str** | The end IP address when adding to the back. | [optional] [readonly] 
**back_start** | **str** | The start IP address when adding to the back. | [optional] [readonly] 
**both_end** | **str** | The end IP address when adding to the back. | [optional] [readonly] 
**both_start** | **str** | The start IP address when adding to both front and back. | [optional] [readonly] 
**front_end** | **str** | The end IP address when adding to the front. | [optional] [readonly] 
**front_start** | **str** | The start IP address when adding to the front. | [optional] [readonly] 
**growth** | **int** | Calculated number of addresses to grow range; its value is determined by asm_config growth factor, type, and min_unused after the expansion. | [optional] [readonly] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**lookahead** | **int** | Either the value from the ASM configuration or -1 if the estimate is that utilization will not exceed the threshold. | [optional] [readonly] 
**range_end** | **str** | The end IP address of the range. | [optional] 
**range_id** | **str** | The resource identifier. | [optional] 
**range_start** | **str** | The start IP address of the range. | [optional] 
**subnet_address** | **str** | The suggested subnet expansion. | [optional] [readonly] 
**subnet_cidr** | **int** | The CIDR of the subnet. | [optional] [readonly] 
**subnet_direction** | **str** | Indicates where the subnet may expand. As the subnet can only be expanded by one bit at a time, it can only grow in one of the two directions. It is set to _none_ if the subnet can&#39;t be expanded.  Valid values are: * _front_ * _back_ * _none_ | [optional] [readonly] 
**subnet_id** | **str** | The resource identifier. | 
**subnet_range** | **str** | The resource identifier. | [optional] 
**subnet_range_end** | **str** | The suggested new range end in expanded subnet. | [optional] [readonly] 
**subnet_range_start** | **str** | The suggested new range start in expanded subnet. | [optional] [readonly] 
**suppress** | **str** | Indicates if future notifications for this subnet should be suppressed.  Valid values are: * _no_ * _time_ * _permanent_  If set to _permanent_ notifications are suppressed until the administrator modifies the configuration for the subnet. If set to _time_ notifications are suppressed until the specified time. Defaults to _no_. | [optional] 
**suppress_time** | **int** | The time duration in days to suppress the notifications for this subnet. | [optional] 
**threshold_utilization** | **int** | The utilization threshold as per ASM configuration. | [optional] [readonly] 
**update** | **str** | The object to update.  Valid values are: * _range_ * _subnet_ * _none_ | [optional] 
**utilization** | **int** | The utilization of DHCP addresses in the subnet. | [optional] [readonly] 

## Example

```python
from ipam.models.asm import ASM

# TODO update the JSON string below
json = "{}"
# create an instance of ASM from a JSON string
asm_instance = ASM.from_json(json)
# print the JSON string representation of the object
print(ASM.to_json())

# convert the object into a dict
asm_dict = asm_instance.to_dict()
# create an instance of ASM from a dict
asm_from_dict = ASM.from_dict(asm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


