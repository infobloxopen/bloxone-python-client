# CreateMaintenanceWindowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | [**CreateMaintenanceWindow**](CreateMaintenanceWindow.md) |  | [optional] 

## Example

```python
from upgrade_policy.models.create_maintenance_window_request import CreateMaintenanceWindowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMaintenanceWindowRequest from a JSON string
create_maintenance_window_request_instance = CreateMaintenanceWindowRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMaintenanceWindowRequest.to_json())

# convert the object into a dict
create_maintenance_window_request_dict = create_maintenance_window_request_instance.to_dict()
# create an instance of CreateMaintenanceWindowRequest from a dict
create_maintenance_window_request_from_dict = CreateMaintenanceWindowRequest.from_dict(create_maintenance_window_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


