# DeferredWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**enabled** | **bool** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from upgrade_policy.models.deferred_window import DeferredWindow

# TODO update the JSON string below
json = "{}"
# create an instance of DeferredWindow from a JSON string
deferred_window_instance = DeferredWindow.from_json(json)
# print the JSON string representation of the object
print(DeferredWindow.to_json())

# convert the object into a dict
deferred_window_dict = deferred_window_instance.to_dict()
# create an instance of DeferredWindow from a dict
deferred_window_from_dict = DeferredWindow.from_dict(deferred_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


