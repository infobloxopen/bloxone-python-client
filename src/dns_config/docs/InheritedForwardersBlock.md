# InheritedForwardersBlock

Inheritance block for fields: _forwarders_, _forwarders_only_, _use_root_forwarders_for_local_resolution_with_b1td_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Defaults to _inherit_. | [optional] 
**display_name** | **str** | Human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | [**ForwardersBlock**](ForwardersBlock.md) |  | [optional] 

## Example

```python
from dns_config.models.inherited_forwarders_block import InheritedForwardersBlock

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedForwardersBlock from a JSON string
inherited_forwarders_block_instance = InheritedForwardersBlock.from_json(json)
# print the JSON string representation of the object
print(InheritedForwardersBlock.to_json())

# convert the object into a dict
inherited_forwarders_block_dict = inherited_forwarders_block_instance.to_dict()
# create an instance of InheritedForwardersBlock from a dict
inherited_forwarders_block_from_dict = InheritedForwardersBlock.from_dict(inherited_forwarders_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


