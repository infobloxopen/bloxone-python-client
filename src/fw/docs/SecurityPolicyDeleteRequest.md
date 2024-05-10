# SecurityPolicyDeleteRequest

The Security Policy delete request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | The list of Security Policy object identifiers. | [optional] 

## Example

```python
from fw.models.security_policy_delete_request import SecurityPolicyDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPolicyDeleteRequest from a JSON string
security_policy_delete_request_instance = SecurityPolicyDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(SecurityPolicyDeleteRequest.to_json())

# convert the object into a dict
security_policy_delete_request_dict = security_policy_delete_request_instance.to_dict()
# create an instance of SecurityPolicyDeleteRequest from a dict
security_policy_delete_request_from_dict = SecurityPolicyDeleteRequest.from_dict(security_policy_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


