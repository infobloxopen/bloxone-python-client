# UpdateMaintenanceWindowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional] 

## Example

```python
from upgrade_policy.models.update_maintenance_window_response import UpdateMaintenanceWindowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMaintenanceWindowResponse from a JSON string
update_maintenance_window_response_instance = UpdateMaintenanceWindowResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateMaintenanceWindowResponse.to_json())

# convert the object into a dict
update_maintenance_window_response_dict = update_maintenance_window_response_instance.to_dict()
# create an instance of UpdateMaintenanceWindowResponse from a dict
update_maintenance_window_response_from_dict = UpdateMaintenanceWindowResponse.from_dict(update_maintenance_window_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


