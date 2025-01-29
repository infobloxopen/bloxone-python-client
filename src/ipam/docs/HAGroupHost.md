# HAGroupHost

An __HAGroupHost__ object (_dhcp/ha_group_host_) represents an on-prem host belonging to an HA Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address on which this host listens. | [optional] 
**heartbeats** | [**List[HAGroupHeartbeats]**](HAGroupHeartbeats.md) | Last successful heartbeat received from its peer/s. This field is set when the _collect_stats_ is set to _true_ in the _GET_ _/dhcp/ha_group_ request. | [optional] 
**host** | **str** | The resource identifier. | 
**port** | **int** | The HA port. | [optional] [readonly] 
**port_v6** | **int** | The HA port used for IPv6 communication. | [optional] [readonly] 
**role** | **str** | The role of this host in the HA relationship: _active_ or _passive_. | [optional] 
**state** | **str** | The state of DHCP on the host. This field is set when the _collect_stats_ is set to _true_ in the _GET_ _/dhcp/ha_group_ request. | [optional] 
**state_v6** | **str** | The state of DHCPv6 on the host. This field is set when the _collect_stats_ is set to _true_ in the _GET_ _/dhcp/ha_group_ request. | [optional] 

## Example

```python
from ipam.models.ha_group_host import HAGroupHost

# TODO update the JSON string below
json = "{}"
# create an instance of HAGroupHost from a JSON string
ha_group_host_instance = HAGroupHost.from_json(json)
# print the JSON string representation of the object
print(HAGroupHost.to_json())

# convert the object into a dict
ha_group_host_dict = ha_group_host_instance.to_dict()
# create an instance of HAGroupHost from a dict
ha_group_host_from_dict = HAGroupHost.from_dict(ha_group_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


