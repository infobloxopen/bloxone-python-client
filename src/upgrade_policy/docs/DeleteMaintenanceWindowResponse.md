# DeleteMaintenanceWindowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window_type** | **str** |  | [optional] 

## Example

```python
from upgrade_policy.models.delete_maintenance_window_response import DeleteMaintenanceWindowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMaintenanceWindowResponse from a JSON string
delete_maintenance_window_response_instance = DeleteMaintenanceWindowResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteMaintenanceWindowResponse.to_json())

# convert the object into a dict
delete_maintenance_window_response_dict = delete_maintenance_window_response_instance.to_dict()
# create an instance of DeleteMaintenanceWindowResponse from a dict
delete_maintenance_window_response_from_dict = DeleteMaintenanceWindowResponse.from_dict(delete_maintenance_window_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


