# ApproveCSRRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_code** | **str** |  | [optional] 

## Example

```python
from infra_provision.models.approve_csr_request import ApproveCSRRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveCSRRequest from a JSON string
approve_csr_request_instance = ApproveCSRRequest.from_json(json)
# print the JSON string representation of the object
print(ApproveCSRRequest.to_json())

# convert the object into a dict
approve_csr_request_dict = approve_csr_request_instance.to_dict()
# create an instance of ApproveCSRRequest from a dict
approve_csr_request_from_dict = ApproveCSRRequest.from_dict(approve_csr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


