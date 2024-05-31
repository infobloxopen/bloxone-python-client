# SecurityPolicyCreateResponse

The Security Policy create response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**SecurityPolicy**](SecurityPolicy.md) | The Security Policy object. | [optional] 

## Example

```python
from fw.models.security_policy_create_response import SecurityPolicyCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPolicyCreateResponse from a JSON string
security_policy_create_response_instance = SecurityPolicyCreateResponse.from_json(json)
# print the JSON string representation of the object
print(SecurityPolicyCreateResponse.to_json())

# convert the object into a dict
security_policy_create_response_dict = security_policy_create_response_instance.to_dict()
# create an instance of SecurityPolicyCreateResponse from a dict
security_policy_create_response_from_dict = SecurityPolicyCreateResponse.from_dict(security_policy_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


