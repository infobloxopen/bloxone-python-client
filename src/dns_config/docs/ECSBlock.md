# ECSBlock

Block for fields: _ecs_enabled_, _ecs_forwarding_, _ecs_prefix_v4_, _ecs_prefix_v6_, _ecs_zones_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecs_enabled** | **bool** | Optional. Field config for _ecs_enabled_ field. | [optional] 
**ecs_forwarding** | **bool** | Optional. Field config for _ecs_forwarding_ field. | [optional] 
**ecs_prefix_v4** | **int** | Optional. Field config for _ecs_prefix_v4_ field. | [optional] 
**ecs_prefix_v6** | **int** | Optional. Field config for _ecs_prefix_v6_ field. | [optional] 
**ecs_zones** | [**List[ECSZone]**](ECSZone.md) | Optional. Field config for _ecs_zones_ field. | [optional] 

## Example

```python
from dns_config.models.ecs_block import ECSBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ECSBlock from a JSON string
ecs_block_instance = ECSBlock.from_json(json)
# print the JSON string representation of the object
print(ECSBlock.to_json())

# convert the object into a dict
ecs_block_dict = ecs_block_instance.to_dict()
# create an instance of ECSBlock from a dict
ecs_block_from_dict = ECSBlock.from_dict(ecs_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


