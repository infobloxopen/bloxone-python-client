# InheritanceAssignedHost

_ddi/assigned_host_ represents a BloxOne DDI host assigned to one of the following:  * Subnet (_ipam/subnet_)  * Range (_ipam/range_)  * Fixed Address (_dhcp/fixed_address_)  * Authoritative Zone (_dns/auth_zone_)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The human-readable display name for the host referred to by _ophid_. | [optional] [readonly] 
**host** | **str** | The resource identifier. | [optional] 
**ophid** | **str** | The on-prem host ID. | [optional] [readonly] 

## Example

```python
from ipam.models.inheritance_assigned_host import InheritanceAssignedHost

# TODO update the JSON string below
json = "{}"
# create an instance of InheritanceAssignedHost from a JSON string
inheritance_assigned_host_instance = InheritanceAssignedHost.from_json(json)
# print the JSON string representation of the object
print(InheritanceAssignedHost.to_json())

# convert the object into a dict
inheritance_assigned_host_dict = inheritance_assigned_host_instance.to_dict()
# create an instance of InheritanceAssignedHost from a dict
inheritance_assigned_host_from_dict = InheritanceAssignedHost.from_dict(inheritance_assigned_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


