# NetAddrPolicyAssignment

network address with the assigned policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addr_net** | **str** | network address in IPv4 CIDR (address/bitmask length) string format | [optional] 
**policy_id** | **int** | Identifier of the security policy associated with this address block | [optional] 

## Example

```python
from dfp.models.net_addr_policy_assignment import NetAddrPolicyAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of NetAddrPolicyAssignment from a JSON string
net_addr_policy_assignment_instance = NetAddrPolicyAssignment.from_json(json)
# print the JSON string representation of the object
print(NetAddrPolicyAssignment.to_json())

# convert the object into a dict
net_addr_policy_assignment_dict = net_addr_policy_assignment_instance.to_dict()
# create an instance of NetAddrPolicyAssignment from a dict
net_addr_policy_assignment_from_dict = NetAddrPolicyAssignment.from_dict(net_addr_policy_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


