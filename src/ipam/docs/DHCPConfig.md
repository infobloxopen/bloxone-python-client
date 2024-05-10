# DHCPConfig

A DHCP Config object (_dhcp/dhcp_config_) represents a shared DHCP configuration that controls how leases are issued.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandoned_reclaim_time** | **int** | The abandoned reclaim time in seconds for IPV4 clients. | [optional] [default to 3600]
**abandoned_reclaim_time_v6** | **int** | The abandoned reclaim time in seconds for IPV6 clients. | [optional] [default to 3600]
**allow_unknown** | **bool** | Disable to allow leases only for known IPv4 clients, those for which a fixed address is configured. | [optional] [default to True]
**allow_unknown_v6** | **bool** | Disable to allow leases only for known IPV6 clients, those for which a fixed address is configured. | [optional] [default to True]
**echo_client_id** | **bool** | Enable/disable to include/exclude the client id when responding to discover or request. | [optional] [default to False]
**filters** | **List[str]** | The resource identifier. | [optional] 
**filters_v6** | **List[str]** | The resource identifier. | [optional] 
**ignore_client_uid** | **bool** | Enable to ignore the client UID when issuing a DHCP lease. Use this option to prevent assigning two IP addresses for a client which does not have a UID during one phase of PXE boot but acquires one for the other phase. | [optional] [default to False]
**ignore_list** | [**List[IgnoreItem]**](IgnoreItem.md) | The list of clients to ignore requests from. | [optional] 
**lease_time** | **int** | The lease duration in seconds. | [optional] [default to 3600]
**lease_time_v6** | **int** | The lease duration in seconds for IPV6 clients. | [optional] [default to 3600]

## Example

```python
from ipam.models.dhcp_config import DHCPConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPConfig from a JSON string
dhcp_config_instance = DHCPConfig.from_json(json)
# print the JSON string representation of the object
print(DHCPConfig.to_json())

# convert the object into a dict
dhcp_config_dict = dhcp_config_instance.to_dict()
# create an instance of DHCPConfig from a dict
dhcp_config_from_dict = DHCPConfig.from_dict(dhcp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


