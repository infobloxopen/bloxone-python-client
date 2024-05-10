# DHCPInfo

The __DHCPInfo__ object represents the DHCP information associated with an address object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_hostname** | **str** | The DHCP host name associated with this client. | [optional] [readonly] 
**client_hwaddr** | **str** | The hardware address associated with this client. | [optional] [readonly] 
**client_id** | **str** | The ID associated with this client. | [optional] [readonly] 
**end** | **datetime** | The timestamp at which the _state_, when set to _leased_, will be changed to _free_. | [optional] [readonly] 
**fingerprint** | **str** | The DHCP fingerprint for the associated lease. | [optional] [readonly] 
**iaid** | **int** | Identity Association Identifier (IAID) of the lease. Applicable only for DHCPv6. | [optional] [readonly] 
**lease_type** | **str** | Lease type. Applicable only for address under DHCP control. The value can be empty for address not under DHCP control.  Valid values are: * _DHCPv6NonTemporaryAddress_: DHCPv6 non-temporary address (NA) * _DHCPv6TemporaryAddress_: DHCPv6 temporary address (TA) * _DHCPv6PrefixDelegation_: DHCPv6 prefix delegation (PD) * _DHCPv4_: DHCPv4 lease | [optional] [readonly] 
**preferred_lifetime** | **datetime** | The length of time that a valid address is preferred (i.e., the time until deprecation). When the preferred lifetime expires, the address becomes deprecated on the client. It is still considered leased on the server. Applicable only for DHCPv6. | [optional] [readonly] 
**remain** | **int** | The remaining time, in seconds, until which the _state_, when set to _leased_, will remain in that state. | [optional] [readonly] 
**start** | **datetime** | The timestamp at which _state_ was first set to _leased_. | [optional] [readonly] 
**state** | **str** | Indicates the status of this IP address from a DHCP protocol standpoint as:   * _none_: Address is not under DHCP control.   * _free_: Address is under DHCP control but has no lease currently assigned.   * _leased_: Address is under DHCP control and has a lease currently assigned. The lease details are contained in the matching _dhcp/lease_ resource. | [optional] [readonly] 
**state_ts** | **datetime** | The timestamp at which the _state_ was last reported. | [optional] [readonly] 

## Example

```python
from ipam.models.dhcp_info import DHCPInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPInfo from a JSON string
dhcp_info_instance = DHCPInfo.from_json(json)
# print the JSON string representation of the object
print(DHCPInfo.to_json())

# convert the object into a dict
dhcp_info_dict = dhcp_info_instance.to_dict()
# create an instance of DHCPInfo from a dict
dhcp_info_from_dict = DHCPInfo.from_dict(dhcp_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


