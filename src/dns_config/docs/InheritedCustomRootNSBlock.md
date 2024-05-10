# InheritedCustomRootNSBlock

Inheritance block for fields: _custom_root_ns_enabled_, _custom_root_ns_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Defaults to _inherit_. | [optional] 
**display_name** | **str** | Human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | [**CustomRootNSBlock**](CustomRootNSBlock.md) |  | [optional] 

## Example

```python
from dns_config.models.inherited_custom_root_ns_block import InheritedCustomRootNSBlock

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedCustomRootNSBlock from a JSON string
inherited_custom_root_ns_block_instance = InheritedCustomRootNSBlock.from_json(json)
# print the JSON string representation of the object
print(InheritedCustomRootNSBlock.to_json())

# convert the object into a dict
inherited_custom_root_ns_block_dict = inherited_custom_root_ns_block_instance.to_dict()
# create an instance of InheritedCustomRootNSBlock from a dict
inherited_custom_root_ns_block_from_dict = InheritedCustomRootNSBlock.from_dict(inherited_custom_root_ns_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


