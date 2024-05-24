# UpdateMaintenanceWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deferred_window** | [**DeferredWindow**](DeferredWindow.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**scheduled_window** | [**ScheduledWindow**](ScheduledWindow.md) |  | [optional] 
**tags** | **object** |  | [optional] 

## Example

```python
from upgrade_policy.models.update_maintenance_window import UpdateMaintenanceWindow

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMaintenanceWindow from a JSON string
update_maintenance_window_instance = UpdateMaintenanceWindow.from_json(json)
# print the JSON string representation of the object
print(UpdateMaintenanceWindow.to_json())

# convert the object into a dict
update_maintenance_window_dict = update_maintenance_window_instance.to_dict()
# create an instance of UpdateMaintenanceWindow from a dict
update_maintenance_window_from_dict = UpdateMaintenanceWindow.from_dict(update_maintenance_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


