# AppApprovalsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**ProtobufFieldMask**](ProtobufFieldMask.md) | Field Mask. | [optional] 
**inserted_approvals** | [**List[AppApproval]**](AppApproval.md) |  | [optional] 
**removed_approvals** | [**List[AppApprovalRemovalRequest]**](AppApprovalRemovalRequest.md) |  | [optional] 

## Example

```python
from fw.models.app_approvals_update_request import AppApprovalsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppApprovalsUpdateRequest from a JSON string
app_approvals_update_request_instance = AppApprovalsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AppApprovalsUpdateRequest.to_json())

# convert the object into a dict
app_approvals_update_request_dict = app_approvals_update_request_instance.to_dict()
# create an instance of AppApprovalsUpdateRequest from a dict
app_approvals_update_request_from_dict = AppApprovalsUpdateRequest.from_dict(app_approvals_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


