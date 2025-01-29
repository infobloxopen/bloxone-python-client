# RealmsConflict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**federated_realms** | **List[str]** | List of __FederatedRealm__ object ids. | [optional] 
**ip_space** | **str** | The resource identifier. | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from ipam.models.realms_conflict import RealmsConflict

# TODO update the JSON string below
json = "{}"
# create an instance of RealmsConflict from a JSON string
realms_conflict_instance = RealmsConflict.from_json(json)
# print the JSON string representation of the object
print(RealmsConflict.to_json())

# convert the object into a dict
realms_conflict_dict = realms_conflict_instance.to_dict()
# create an instance of RealmsConflict from a dict
realms_conflict_from_dict = RealmsConflict.from_dict(realms_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


