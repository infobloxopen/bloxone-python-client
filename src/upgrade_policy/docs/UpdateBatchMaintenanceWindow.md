# UpdateBatchMaintenanceWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deferred_window** | [**DeferredWindow**](DeferredWindow.md) |  | [optional] 
**mw_id** | **str** |  | [optional] 
**scheduled_window** | [**ScheduledWindow**](ScheduledWindow.md) |  | [optional] 
**tags** | **object** |  | [optional] 

## Example

```python
from upgrade_policy.models.update_batch_maintenance_window import UpdateBatchMaintenanceWindow

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBatchMaintenanceWindow from a JSON string
update_batch_maintenance_window_instance = UpdateBatchMaintenanceWindow.from_json(json)
# print the JSON string representation of the object
print(UpdateBatchMaintenanceWindow.to_json())

# convert the object into a dict
update_batch_maintenance_window_dict = update_batch_maintenance_window_instance.to_dict()
# create an instance of UpdateBatchMaintenanceWindow from a dict
update_batch_maintenance_window_from_dict = UpdateBatchMaintenanceWindow.from_dict(update_batch_maintenance_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


