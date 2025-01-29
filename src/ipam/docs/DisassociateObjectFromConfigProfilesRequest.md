# DisassociateObjectFromConfigProfilesRequest

DisassociateObjectToConfigProfiles disassociates an object to config profiles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_profile_ids** | **List[str]** | The resource identifier. | 
**fields** | [**ProtobufFieldMask**](ProtobufFieldMask.md) |  | [optional] 
**object_id** | **str** | The resource identifier. | 

## Example

```python
from ipam.models.disassociate_object_from_config_profiles_request import DisassociateObjectFromConfigProfilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisassociateObjectFromConfigProfilesRequest from a JSON string
disassociate_object_from_config_profiles_request_instance = DisassociateObjectFromConfigProfilesRequest.from_json(json)
# print the JSON string representation of the object
print(DisassociateObjectFromConfigProfilesRequest.to_json())

# convert the object into a dict
disassociate_object_from_config_profiles_request_dict = disassociate_object_from_config_profiles_request_instance.to_dict()
# create an instance of DisassociateObjectFromConfigProfilesRequest from a dict
disassociate_object_from_config_profiles_request_from_dict = DisassociateObjectFromConfigProfilesRequest.from_dict(disassociate_object_from_config_profiles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


