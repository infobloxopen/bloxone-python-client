# DHCPPacketStats

The DHCPPacketStats object represents DHCP packets statistics for a DHCP __Host__.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_pkt_received** | **str** | The number of DHCP packets received. | [optional] [readonly] 
**dhcp_pkt_received_v6** | **str** | The number of DHCP V6 packets received. | [optional] [readonly] 
**dhcp_pkt_sent** | **str** | The number of DHCP packets sent. | [optional] [readonly] 
**dhcp_pkt_sent_v6** | **str** | The number of DHCP V6 packets sent. | [optional] [readonly] 
**dhcp_req_received** | **str** | The number of DHCP requests received. | [optional] [readonly] 
**dhcp_req_received_v6** | **str** | The number of DHCP V6 requests received. | [optional] [readonly] 

## Example

```python
from ipam.models.dhcp_packet_stats import DHCPPacketStats

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPPacketStats from a JSON string
dhcp_packet_stats_instance = DHCPPacketStats.from_json(json)
# print the JSON string representation of the object
print(DHCPPacketStats.to_json())

# convert the object into a dict
dhcp_packet_stats_dict = dhcp_packet_stats_instance.to_dict()
# create an instance of DHCPPacketStats from a dict
dhcp_packet_stats_from_dict = DHCPPacketStats.from_dict(dhcp_packet_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


