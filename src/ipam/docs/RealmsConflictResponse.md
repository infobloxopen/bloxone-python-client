# RealmsConflictResponse

The response format to retrieve Realms Conflict objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[RealmsConflict]**](RealmsConflict.md) | List of conflicts across _ipam/ip_space_ objects. | [optional] 

## Example

```python
from ipam.models.realms_conflict_response import RealmsConflictResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RealmsConflictResponse from a JSON string
realms_conflict_response_instance = RealmsConflictResponse.from_json(json)
# print the JSON string representation of the object
print(RealmsConflictResponse.to_json())

# convert the object into a dict
realms_conflict_response_dict = realms_conflict_response_instance.to_dict()
# create an instance of RealmsConflictResponse from a dict
realms_conflict_response_from_dict = RealmsConflictResponse.from_dict(realms_conflict_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


