# InheritedECSBlock

Inheritance block for fields: _ecs_enabled_, _ecs_forwarding_, _ecs_prefix_v4_, _ecs_prefix_v6_, _ecs_zones_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Defaults to _inherit_. | [optional] 
**display_name** | **str** | Human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | [**ECSBlock**](ECSBlock.md) | Inherited value. | [optional] [readonly] 

## Example

```python
from dns_config.models.inherited_ecs_block import InheritedECSBlock

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedECSBlock from a JSON string
inherited_ecs_block_instance = InheritedECSBlock.from_json(json)
# print the JSON string representation of the object
print(InheritedECSBlock.to_json())

# convert the object into a dict
inherited_ecs_block_dict = inherited_ecs_block_instance.to_dict()
# create an instance of InheritedECSBlock from a dict
inherited_ecs_block_from_dict = InheritedECSBlock.from_dict(inherited_ecs_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


