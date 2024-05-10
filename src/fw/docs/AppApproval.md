# AppApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** | The name of the application, should be unique and is used as Application Identifier | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fw.models.app_approval import AppApproval

# TODO update the JSON string below
json = "{}"
# create an instance of AppApproval from a JSON string
app_approval_instance = AppApproval.from_json(json)
# print the JSON string representation of the object
print(AppApproval.to_json())

# convert the object into a dict
app_approval_dict = app_approval_instance.to_dict()
# create an instance of AppApproval from a dict
app_approval_from_dict = AppApproval.from_dict(app_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


