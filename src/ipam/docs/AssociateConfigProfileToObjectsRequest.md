# AssociateConfigProfileToObjectsRequest

AssociateConfigProfileToObjects associates a config profile to its objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_profile_id** | **str** | The resource identifier. | 
**fields** | [**ProtobufFieldMask**](ProtobufFieldMask.md) |  | [optional] 
**object_ids** | **List[str]** | The resource identifier. | 

## Example

```python
from ipam.models.associate_config_profile_to_objects_request import AssociateConfigProfileToObjectsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssociateConfigProfileToObjectsRequest from a JSON string
associate_config_profile_to_objects_request_instance = AssociateConfigProfileToObjectsRequest.from_json(json)
# print the JSON string representation of the object
print(AssociateConfigProfileToObjectsRequest.to_json())

# convert the object into a dict
associate_config_profile_to_objects_request_dict = associate_config_profile_to_objects_request_instance.to_dict()
# create an instance of AssociateConfigProfileToObjectsRequest from a dict
associate_config_profile_to_objects_request_from_dict = AssociateConfigProfileToObjectsRequest.from_dict(associate_config_profile_to_objects_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


