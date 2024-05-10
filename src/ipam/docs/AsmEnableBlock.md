# AsmEnableBlock

ASM enable group of fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Indicates whether Automated Scope Management is enabled or not. | [optional] 
**enable_notification** | **bool** | Indicates whether sending notifications to the users is enabled or not. | [optional] 
**reenable_date** | **datetime** | The date at which notifications will be re-enabled automatically. | [optional] 

## Example

```python
from ipam.models.asm_enable_block import AsmEnableBlock

# TODO update the JSON string below
json = "{}"
# create an instance of AsmEnableBlock from a JSON string
asm_enable_block_instance = AsmEnableBlock.from_json(json)
# print the JSON string representation of the object
print(AsmEnableBlock.to_json())

# convert the object into a dict
asm_enable_block_dict = asm_enable_block_instance.to_dict()
# create an instance of AsmEnableBlock from a dict
asm_enable_block_from_dict = AsmEnableBlock.from_dict(asm_enable_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


