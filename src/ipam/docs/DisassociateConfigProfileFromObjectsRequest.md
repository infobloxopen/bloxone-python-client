# DisassociateConfigProfileFromObjectsRequest

DisassociateConfigProfileToObjects disassociates an object to config profiles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_profile_id** | **str** | The resource identifier. | 
**fields** | [**ProtobufFieldMask**](ProtobufFieldMask.md) |  | [optional] 
**object_ids** | **List[str]** | The resource identifier. | 

## Example

```python
from ipam.models.disassociate_config_profile_from_objects_request import DisassociateConfigProfileFromObjectsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisassociateConfigProfileFromObjectsRequest from a JSON string
disassociate_config_profile_from_objects_request_instance = DisassociateConfigProfileFromObjectsRequest.from_json(json)
# print the JSON string representation of the object
print(DisassociateConfigProfileFromObjectsRequest.to_json())

# convert the object into a dict
disassociate_config_profile_from_objects_request_dict = disassociate_config_profile_from_objects_request_instance.to_dict()
# create an instance of DisassociateConfigProfileFromObjectsRequest from a dict
disassociate_config_profile_from_objects_request_from_dict = DisassociateConfigProfileFromObjectsRequest.from_dict(disassociate_config_profile_from_objects_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


