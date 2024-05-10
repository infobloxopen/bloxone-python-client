# SecurityPolicyMultiResponse

The Security Policy list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[SecurityPolicy]**](SecurityPolicy.md) | The list of Security Policy objects. | [optional] 

## Example

```python
from fw.models.security_policy_multi_response import SecurityPolicyMultiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPolicyMultiResponse from a JSON string
security_policy_multi_response_instance = SecurityPolicyMultiResponse.from_json(json)
# print the JSON string representation of the object
print(SecurityPolicyMultiResponse.to_json())

# convert the object into a dict
security_policy_multi_response_dict = security_policy_multi_response_instance.to_dict()
# create an instance of SecurityPolicyMultiResponse from a dict
security_policy_multi_response_from_dict = SecurityPolicyMultiResponse.from_dict(security_policy_multi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


