# UpdateMaintenanceWindowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**payload** | [**UpdateMaintenanceWindow**](UpdateMaintenanceWindow.md) |  | [optional] 

## Example

```python
from upgrade_policy.models.update_maintenance_window_request import UpdateMaintenanceWindowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMaintenanceWindowRequest from a JSON string
update_maintenance_window_request_instance = UpdateMaintenanceWindowRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMaintenanceWindowRequest.to_json())

# convert the object into a dict
update_maintenance_window_request_dict = update_maintenance_window_request_instance.to_dict()
# create an instance of UpdateMaintenanceWindowRequest from a dict
update_maintenance_window_request_from_dict = UpdateMaintenanceWindowRequest.from_dict(update_maintenance_window_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


