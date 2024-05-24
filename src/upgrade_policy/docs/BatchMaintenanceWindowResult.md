# BatchMaintenanceWindowResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_ids** | **List[str]** |  | [optional] 
**updated_mws** | [**List[MaintenanceWindow]**](MaintenanceWindow.md) |  | [optional] 

## Example

```python
from upgrade_policy.models.batch_maintenance_window_result import BatchMaintenanceWindowResult

# TODO update the JSON string below
json = "{}"
# create an instance of BatchMaintenanceWindowResult from a JSON string
batch_maintenance_window_result_instance = BatchMaintenanceWindowResult.from_json(json)
# print the JSON string representation of the object
print(BatchMaintenanceWindowResult.to_json())

# convert the object into a dict
batch_maintenance_window_result_dict = batch_maintenance_window_result_instance.to_dict()
# create an instance of BatchMaintenanceWindowResult from a dict
batch_maintenance_window_result_from_dict = BatchMaintenanceWindowResult.from_dict(batch_maintenance_window_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


