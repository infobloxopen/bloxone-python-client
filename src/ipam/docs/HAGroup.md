# HAGroup

An __HAGroup__ object (_dhcp/ha_group_) represents on-prem hosts that can serve the same leases for HA.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anycast_config_id** | **str** | The resource identifier. | [optional] 
**comment** | **str** | The description for the HA group. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**hosts** | [**List[HAGroupHost]**](HAGroupHost.md) | The list of hosts. | 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**ip_space** | **str** | The resource identifier. | [optional] 
**mode** | **str** | The mode of the HA group.  Valid values are: * _active-active_: Both on-prem hosts remain active. * _active-passive_: One on-prem host remains active and one remains passive. When the active on-prem host is down, the passive on-prem host takes over. * _advanced-active-passive_: One on-prem host may be part of multiple HA groups. When the active on-prem host is down, the passive on-prem host takes over. | [optional] 
**name** | **str** | The name of the HA group. Must contain 1 to 256 characters. Can include UTF-8. | 
**status** | **str** | Status of the HA group. This field is set when the _collect_stats_ is set to _true_ in the _GET_ _/dhcp/ha_group_ request. | [optional] 
**tags** | **object** | The tags for the HA group. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 

## Example

```python
from ipam.models.ha_group import HAGroup

# TODO update the JSON string below
json = "{}"
# create an instance of HAGroup from a JSON string
ha_group_instance = HAGroup.from_json(json)
# print the JSON string representation of the object
print(HAGroup.to_json())

# convert the object into a dict
ha_group_dict = ha_group_instance.to_dict()
# create an instance of HAGroup from a dict
ha_group_from_dict = HAGroup.from_dict(ha_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


