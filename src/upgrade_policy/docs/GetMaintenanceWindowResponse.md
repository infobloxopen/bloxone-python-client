# GetMaintenanceWindowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional] 

## Example

```python
from upgrade_policy.models.get_maintenance_window_response import GetMaintenanceWindowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMaintenanceWindowResponse from a JSON string
get_maintenance_window_response_instance = GetMaintenanceWindowResponse.from_json(json)
# print the JSON string representation of the object
print(GetMaintenanceWindowResponse.to_json())

# convert the object into a dict
get_maintenance_window_response_dict = get_maintenance_window_response_instance.to_dict()
# create an instance of GetMaintenanceWindowResponse from a dict
get_maintenance_window_response_from_dict = GetMaintenanceWindowResponse.from_dict(get_maintenance_window_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


