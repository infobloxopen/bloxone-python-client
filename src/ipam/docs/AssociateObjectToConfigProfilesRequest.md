# AssociateObjectToConfigProfilesRequest

AssociateObjectToConfigProfiles associates an object to config profiles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_profile_ids** | **List[str]** | The resource identifier. | 
**fields** | [**ProtobufFieldMask**](ProtobufFieldMask.md) |  | [optional] 
**object_id** | **str** | The resource identifier. | 

## Example

```python
from ipam.models.associate_object_to_config_profiles_request import AssociateObjectToConfigProfilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssociateObjectToConfigProfilesRequest from a JSON string
associate_object_to_config_profiles_request_instance = AssociateObjectToConfigProfilesRequest.from_json(json)
# print the JSON string representation of the object
print(AssociateObjectToConfigProfilesRequest.to_json())

# convert the object into a dict
associate_object_to_config_profiles_request_dict = associate_object_to_config_profiles_request_instance.to_dict()
# create an instance of AssociateObjectToConfigProfilesRequest from a dict
associate_object_to_config_profiles_request_from_dict = AssociateObjectToConfigProfilesRequest.from_dict(associate_object_to_config_profiles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


