# AuthZoneConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_primaries** | [**List[ExternalPrimary]**](ExternalPrimary.md) | Optional. DNS primaries external to BloxOne DDI. Order is not significant. | [optional] 
**external_secondaries** | [**List[ExternalSecondary]**](ExternalSecondary.md) | DNS secondaries external to BloxOne DDI. Order is not significant. | [optional] 
**internal_secondaries** | [**List[InternalSecondary]**](InternalSecondary.md) | Optional. BloxOne DDI hosts acting as internal secondaries. Order is not significant. | [optional] 
**nsgs** | **List[str]** | The resource identifier. | [optional] 

## Example

```python
from dns_config.models.auth_zone_config import AuthZoneConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AuthZoneConfig from a JSON string
auth_zone_config_instance = AuthZoneConfig.from_json(json)
# print the JSON string representation of the object
print(AuthZoneConfig.to_json())

# convert the object into a dict
auth_zone_config_dict = auth_zone_config_instance.to_dict()
# create an instance of AuthZoneConfig from a dict
auth_zone_config_from_dict = AuthZoneConfig.from_dict(auth_zone_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


