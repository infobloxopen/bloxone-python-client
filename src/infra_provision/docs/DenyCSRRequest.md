# DenyCSRRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_code** | **str** |  | [optional] 

## Example

```python
from infra_provision.models.deny_csr_request import DenyCSRRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DenyCSRRequest from a JSON string
deny_csr_request_instance = DenyCSRRequest.from_json(json)
# print the JSON string representation of the object
print(DenyCSRRequest.to_json())

# convert the object into a dict
deny_csr_request_dict = deny_csr_request_instance.to_dict()
# create an instance of DenyCSRRequest from a dict
deny_csr_request_from_dict = DenyCSRRequest.from_dict(deny_csr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


