# HAGroupHeartbeats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peer** | **str** | The name of the peer. | [optional] 
**successful_heartbeat** | **str** | The timestamp as a string of the last successful heartbeat received from the peer above. | [optional] 

## Example

```python
from ipam.models.ha_group_heartbeats import HAGroupHeartbeats

# TODO update the JSON string below
json = "{}"
# create an instance of HAGroupHeartbeats from a JSON string
ha_group_heartbeats_instance = HAGroupHeartbeats.from_json(json)
# print the JSON string representation of the object
print(HAGroupHeartbeats.to_json())

# convert the object into a dict
ha_group_heartbeats_dict = ha_group_heartbeats_instance.to_dict()
# create an instance of HAGroupHeartbeats from a dict
ha_group_heartbeats_from_dict = HAGroupHeartbeats.from_dict(ha_group_heartbeats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


