# BatchMaintenanceWindowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | [**BatchMaintenanceWindow**](BatchMaintenanceWindow.md) |  | [optional] 

## Example

```python
from upgrade_policy.models.batch_maintenance_window_request import BatchMaintenanceWindowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchMaintenanceWindowRequest from a JSON string
batch_maintenance_window_request_instance = BatchMaintenanceWindowRequest.from_json(json)
# print the JSON string representation of the object
print(BatchMaintenanceWindowRequest.to_json())

# convert the object into a dict
batch_maintenance_window_request_dict = batch_maintenance_window_request_instance.to_dict()
# create an instance of BatchMaintenanceWindowRequest from a dict
batch_maintenance_window_request_from_dict = BatchMaintenanceWindowRequest.from_dict(batch_maintenance_window_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


