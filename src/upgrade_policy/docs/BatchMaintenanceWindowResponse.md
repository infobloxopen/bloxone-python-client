# BatchMaintenanceWindowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**BatchMaintenanceWindowResult**](BatchMaintenanceWindowResult.md) |  | [optional] 

## Example

```python
from upgrade_policy.models.batch_maintenance_window_response import BatchMaintenanceWindowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchMaintenanceWindowResponse from a JSON string
batch_maintenance_window_response_instance = BatchMaintenanceWindowResponse.from_json(json)
# print the JSON string representation of the object
print(BatchMaintenanceWindowResponse.to_json())

# convert the object into a dict
batch_maintenance_window_response_dict = batch_maintenance_window_response_instance.to_dict()
# create an instance of BatchMaintenanceWindowResponse from a dict
batch_maintenance_window_response_from_dict = BatchMaintenanceWindowResponse.from_dict(batch_maintenance_window_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


