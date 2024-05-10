# AppApprovalRemovalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 

## Example

```python
from fw.models.app_approval_removal_request import AppApprovalRemovalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppApprovalRemovalRequest from a JSON string
app_approval_removal_request_instance = AppApprovalRemovalRequest.from_json(json)
# print the JSON string representation of the object
print(AppApprovalRemovalRequest.to_json())

# convert the object into a dict
app_approval_removal_request_dict = app_approval_removal_request_instance.to_dict()
# create an instance of AppApprovalRemovalRequest from a dict
app_approval_removal_request_from_dict = AppApprovalRemovalRequest.from_dict(app_approval_removal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


