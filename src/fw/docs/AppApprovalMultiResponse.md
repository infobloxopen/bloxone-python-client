# AppApprovalMultiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AppApproval]**](AppApproval.md) |  | [optional] 

## Example

```python
from fw.models.app_approval_multi_response import AppApprovalMultiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppApprovalMultiResponse from a JSON string
app_approval_multi_response_instance = AppApprovalMultiResponse.from_json(json)
# print the JSON string representation of the object
print(AppApprovalMultiResponse.to_json())

# convert the object into a dict
app_approval_multi_response_dict = app_approval_multi_response_instance.to_dict()
# create an instance of AppApprovalMultiResponse from a dict
app_approval_multi_response_from_dict = AppApprovalMultiResponse.from_dict(app_approval_multi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


