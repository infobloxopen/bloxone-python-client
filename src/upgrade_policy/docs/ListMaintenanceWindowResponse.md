# ListMaintenanceWindowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[MaintenanceWindow]**](MaintenanceWindow.md) |  | [optional] 

## Example

```python
from upgrade_policy.models.list_maintenance_window_response import ListMaintenanceWindowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListMaintenanceWindowResponse from a JSON string
list_maintenance_window_response_instance = ListMaintenanceWindowResponse.from_json(json)
# print the JSON string representation of the object
print(ListMaintenanceWindowResponse.to_json())

# convert the object into a dict
list_maintenance_window_response_dict = list_maintenance_window_response_instance.to_dict()
# create an instance of ListMaintenanceWindowResponse from a dict
list_maintenance_window_response_from_dict = ListMaintenanceWindowResponse.from_dict(list_maintenance_window_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


