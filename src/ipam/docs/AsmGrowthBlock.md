# AsmGrowthBlock

ASM growth group of fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**growth_factor** | **int** | Either the number or percentage of addresses to grow by. | [optional] 
**growth_type** | **str** | The type of factor to use: _percent_ or _count_. | [optional] 

## Example

```python
from ipam.models.asm_growth_block import AsmGrowthBlock

# TODO update the JSON string below
json = "{}"
# create an instance of AsmGrowthBlock from a JSON string
asm_growth_block_instance = AsmGrowthBlock.from_json(json)
# print the JSON string representation of the object
print(AsmGrowthBlock.to_json())

# convert the object into a dict
asm_growth_block_dict = asm_growth_block_instance.to_dict()
# create an instance of AsmGrowthBlock from a dict
asm_growth_block_from_dict = AsmGrowthBlock.from_dict(asm_growth_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


