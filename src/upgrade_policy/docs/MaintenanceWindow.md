# MaintenanceWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deferred_window** | [**DeferredWindow**](DeferredWindow.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**scheduled_window** | [**ScheduledWindow**](ScheduledWindow.md) |  | [optional] 
**tags** | **object** |  | [optional] 
**window_type** | **str** |  | [optional] [readonly] 

## Example

```python
from upgrade_policy.models.maintenance_window import MaintenanceWindow

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceWindow from a JSON string
maintenance_window_instance = MaintenanceWindow.from_json(json)
# print the JSON string representation of the object
print(MaintenanceWindow.to_json())

# convert the object into a dict
maintenance_window_dict = maintenance_window_instance.to_dict()
# create an instance of MaintenanceWindow from a dict
maintenance_window_from_dict = MaintenanceWindow.from_dict(maintenance_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


