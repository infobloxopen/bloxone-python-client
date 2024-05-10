# AnycastConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**anycast_ip_address** | **str** |  | [optional] 
**anycast_ipv6_address** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**fields** | [**ProtobufFieldMask**](ProtobufFieldMask.md) |  | [optional] 
**id** | **int** |  | [optional] [readonly] 
**is_configured** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**onprem_hosts** | [**List[OnpremHostRef]**](OnpremHostRef.md) |  | [optional] 
**runtime_status** | **str** |  | [optional] 
**service** | **str** |  | [optional] 
**tags** | **object** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from anycast.models.anycast_config import AnycastConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AnycastConfig from a JSON string
anycast_config_instance = AnycastConfig.from_json(json)
# print the JSON string representation of the object
print(AnycastConfig.to_json())

# convert the object into a dict
anycast_config_dict = anycast_config_instance.to_dict()
# create an instance of AnycastConfig from a dict
anycast_config_from_dict = AnycastConfig.from_dict(anycast_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


