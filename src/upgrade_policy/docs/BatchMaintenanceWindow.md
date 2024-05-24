# BatchMaintenanceWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_mws** | [**List[CreateMaintenanceWindow]**](CreateMaintenanceWindow.md) |  | [optional] 
**delete_mws** | **List[str]** |  | [optional] 
**update_mws** | [**List[UpdateBatchMaintenanceWindow]**](UpdateBatchMaintenanceWindow.md) |  | [optional] 

## Example

```python
from upgrade_policy.models.batch_maintenance_window import BatchMaintenanceWindow

# TODO update the JSON string below
json = "{}"
# create an instance of BatchMaintenanceWindow from a JSON string
batch_maintenance_window_instance = BatchMaintenanceWindow.from_json(json)
# print the JSON string representation of the object
print(BatchMaintenanceWindow.to_json())

# convert the object into a dict
batch_maintenance_window_dict = batch_maintenance_window_instance.to_dict()
# create an instance of BatchMaintenanceWindow from a dict
batch_maintenance_window_from_dict = BatchMaintenanceWindow.from_dict(batch_maintenance_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


