# ForwardZoneConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_forwarders** | [**List[Forwarder]**](Forwarder.md) | Optional. External DNS servers to forward to. Order is not significant. | [optional] 
**hosts** | **List[str]** | The resource identifier. | [optional] 
**internal_forwarders** | **List[str]** | The resource identifier. | [optional] 
**nsgs** | **List[str]** | The resource identifier. | [optional] 

## Example

```python
from dns_config.models.forward_zone_config import ForwardZoneConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardZoneConfig from a JSON string
forward_zone_config_instance = ForwardZoneConfig.from_json(json)
# print the JSON string representation of the object
print(ForwardZoneConfig.to_json())

# convert the object into a dict
forward_zone_config_dict = forward_zone_config_instance.to_dict()
# create an instance of ForwardZoneConfig from a dict
forward_zone_config_from_dict = ForwardZoneConfig.from_dict(forward_zone_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


