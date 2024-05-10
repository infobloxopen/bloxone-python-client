# Dfp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **datetime** | The time when this DNS Forwarding Proxy object was created. | [optional] [readonly] 
**elb_ip_list** | **List[str]** | The list of internal or local DNS servers&#39; IPv4 or IPv6 addresses that are used as ELB IPs. | [optional] [readonly] 
**forwarding_policy** | **str** |  | [optional] 
**host** | [**List[DfpHost]**](DfpHost.md) | host information. For internal Use only. | [optional] 
**id** | **int** | The DNS Forwarding Proxy object identifier. | [optional] [readonly] 
**internal_domain_lists** | **List[int]** | The list of internal domains list IDs that are associated with this DFP | [optional] 
**name** | **str** | The name of the DNS Forwarding Proxy. | [optional] [readonly] 
**net_addr_policy_ids** | [**List[NetAddrPolicyAssignment]**](NetAddrPolicyAssignment.md) | List of network-address-scoped security policy assignments | [optional] 
**ophid** | **str** | The On-Prem Host identifier. | [optional] [readonly] 
**policy_id** | **int** | The identifier of the security policy with which the DNS Forwarding Proxy is associated. | [optional] [readonly] 
**pop_region_id** | **int** | Point of Presence (PoP) region | [optional] [readonly] 
**resolvers_all** | [**List[Resolver]**](Resolver.md) |  | [optional] 
**service_id** | **str** | The On-Prem Application Service identifier. For internal Use only | [optional] [readonly] 
**service_name** | **str** | The On-Prem Application Service name. For internal Use only | [optional] [readonly] 
**site_id** | **str** | The DNS Forwarding Proxy site identifier that is appended to DNS queries originating from this DNS Forwarding Proxy and subsequently used for policy lookup purposes. | [optional] [readonly] 
**updated_time** | **datetime** | The time when this DNS Forwarding Proxy object was last updated. | [optional] [readonly] 

## Example

```python
from dfp.models.dfp import Dfp

# TODO update the JSON string below
json = "{}"
# create an instance of Dfp from a JSON string
dfp_instance = Dfp.from_json(json)
# print the JSON string representation of the object
print(Dfp.to_json())

# convert the object into a dict
dfp_dict = dfp_instance.to_dict()
# create an instance of Dfp from a dict
dfp_from_dict = Dfp.from_dict(dfp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


