# ECSZone

EDNS Client Subnet zone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** | Access control for zone.  Allowed values: * _allow_, * _deny_. | 
**fqdn** | **str** | Zone FQDN. | 
**protocol_fqdn** | **str** | Zone FQDN in punycode. | [optional] [readonly] 

## Example

```python
from dns_config.models.ecs_zone import ECSZone

# TODO update the JSON string below
json = "{}"
# create an instance of ECSZone from a JSON string
ecs_zone_instance = ECSZone.from_json(json)
# print the JSON string representation of the object
print(ECSZone.to_json())

# convert the object into a dict
ecs_zone_dict = ecs_zone_instance.to_dict()
# create an instance of ECSZone from a dict
ecs_zone_from_dict = ECSZone.from_dict(ecs_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


