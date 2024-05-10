# Inheritance2AssignedHost

_ddi/assigned_host_ represents a BloxOne DDI host assigned to an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The human-readable display name for the host referred to by _ophid_. | [optional] [readonly] 
**host** | **str** | The resource identifier. | [optional] 
**ophid** | **str** | The on-prem host ID. | [optional] [readonly] 

## Example

```python
from dns_config.models.inheritance2_assigned_host import Inheritance2AssignedHost

# TODO update the JSON string below
json = "{}"
# create an instance of Inheritance2AssignedHost from a JSON string
inheritance2_assigned_host_instance = Inheritance2AssignedHost.from_json(json)
# print the JSON string representation of the object
print(Inheritance2AssignedHost.to_json())

# convert the object into a dict
inheritance2_assigned_host_dict = inheritance2_assigned_host_instance.to_dict()
# create an instance of Inheritance2AssignedHost from a dict
inheritance2_assigned_host_from_dict = Inheritance2AssignedHost.from_dict(inheritance2_assigned_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


