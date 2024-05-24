# ScheduledWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**duration** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**start_time** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**weekday** | **int** |  | [optional] 

## Example

```python
from upgrade_policy.models.scheduled_window import ScheduledWindow

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledWindow from a JSON string
scheduled_window_instance = ScheduledWindow.from_json(json)
# print the JSON string representation of the object
print(ScheduledWindow.to_json())

# convert the object into a dict
scheduled_window_dict = scheduled_window_instance.to_dict()
# create an instance of ScheduledWindow from a dict
scheduled_window_from_dict = ScheduledWindow.from_dict(scheduled_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


