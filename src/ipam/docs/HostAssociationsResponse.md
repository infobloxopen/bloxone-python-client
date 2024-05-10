# HostAssociationsResponse

The response format to retrieve __HAGroup__, __Subnet__ and __DHCPPacketStats__ objects associated with the DHCP __Host__ object. The host in question is also included in the output, for the convenience reasons.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_pkt_stats** | [**DHCPPacketStats**](DHCPPacketStats.md) |  | [optional] 
**ha_groups** | [**List[HAGroup]**](HAGroup.md) | The list of HA groups. | [optional] 
**host** | [**Host**](Host.md) |  | [optional] 
**subnets** | [**List[Subnet]**](Subnet.md) | The list of subnets. | [optional] 

## Example

```python
from ipam.models.host_associations_response import HostAssociationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HostAssociationsResponse from a JSON string
host_associations_response_instance = HostAssociationsResponse.from_json(json)
# print the JSON string representation of the object
print(HostAssociationsResponse.to_json())

# convert the object into a dict
host_associations_response_dict = host_associations_response_instance.to_dict()
# create an instance of HostAssociationsResponse from a dict
host_associations_response_from_dict = HostAssociationsResponse.from_dict(host_associations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


