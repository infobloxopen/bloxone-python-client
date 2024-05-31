# AppApprovalsReplaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvals** | [**List[AppApproval]**](AppApproval.md) |  | [optional] 
**fields** | [**ProtobufFieldMask**](ProtobufFieldMask.md) | Field Mask. | [optional] 

## Example

```python
from fw.models.app_approvals_replace_request import AppApprovalsReplaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppApprovalsReplaceRequest from a JSON string
app_approvals_replace_request_instance = AppApprovalsReplaceRequest.from_json(json)
# print the JSON string representation of the object
print(AppApprovalsReplaceRequest.to_json())

# convert the object into a dict
app_approvals_replace_request_dict = app_approvals_replace_request_instance.to_dict()
# create an instance of AppApprovalsReplaceRequest from a dict
app_approvals_replace_request_from_dict = AppApprovalsReplaceRequest.from_dict(app_approvals_replace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


