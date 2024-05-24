# CreateMaintenanceWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deferred_window** | [**DeferredWindow**](DeferredWindow.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**scheduled_window** | [**ScheduledWindow**](ScheduledWindow.md) |  | [optional] 
**tags** | **object** |  | [optional] 
**window_type** | **str** |  | [optional] 

## Example

```python
from upgrade_policy.models.create_maintenance_window import CreateMaintenanceWindow

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMaintenanceWindow from a JSON string
create_maintenance_window_instance = CreateMaintenanceWindow.from_json(json)
# print the JSON string representation of the object
print(CreateMaintenanceWindow.to_json())

# convert the object into a dict
create_maintenance_window_dict = create_maintenance_window_instance.to_dict()
# create an instance of CreateMaintenanceWindow from a dict
create_maintenance_window_from_dict = CreateMaintenanceWindow.from_dict(create_maintenance_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


