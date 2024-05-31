# NetAddrDfpAssignment

Scoped DFP assignment to a policy, scoped via network address (CIDR)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addr_net** | **str** | network address in IPv4 CIDR (address/bitmask length) string format | [optional] 
**dfp_ids** | **List[int]** | The list of identifiers of DFPs that have association with this scope. | [optional] [readonly] 
**dfp_service_ids** | **List[str]** |  | [optional] [readonly] 
**end** | **str** |  | [optional] 
**external_scope_id** | **str** | external scope ID, UUID | [optional] 
**host_id** | **str** | Host reference, UUID | [optional] 
**ip_space_id** | **str** | IPSpace reference, UUID | [optional] 
**scope_type** | [**NetAddrDfpAssignmentScopeType**](NetAddrDfpAssignmentScopeType.md) | scope type | [optional] 
**start** | **str** | Start and end pair of addresses used for range scope type | [optional] 

## Example

```python
from fw.models.net_addr_dfp_assignment import NetAddrDfpAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of NetAddrDfpAssignment from a JSON string
net_addr_dfp_assignment_instance = NetAddrDfpAssignment.from_json(json)
# print the JSON string representation of the object
print(NetAddrDfpAssignment.to_json())

# convert the object into a dict
net_addr_dfp_assignment_dict = net_addr_dfp_assignment_instance.to_dict()
# create an instance of NetAddrDfpAssignment from a dict
net_addr_dfp_assignment_from_dict = NetAddrDfpAssignment.from_dict(net_addr_dfp_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


