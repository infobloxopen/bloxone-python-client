# CustomRootNSBlock

Block for fields: _custom_root_ns_enabled_, _custom_root_ns_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_root_ns** | [**List[RootNS]**](RootNS.md) | Optional. Field config for _custom_root_ns_ field. | [optional] 
**custom_root_ns_enabled** | **bool** | Optional. Field config for _custom_root_ns_enabled_ field. | [optional] 

## Example

```python
from dns_config.models.custom_root_ns_block import CustomRootNSBlock

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRootNSBlock from a JSON string
custom_root_ns_block_instance = CustomRootNSBlock.from_json(json)
# print the JSON string representation of the object
print(CustomRootNSBlock.to_json())

# convert the object into a dict
custom_root_ns_block_dict = custom_root_ns_block_instance.to_dict()
# create an instance of CustomRootNSBlock from a dict
custom_root_ns_block_from_dict = CustomRootNSBlock.from_dict(custom_root_ns_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


