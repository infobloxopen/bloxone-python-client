# SecurityPolicyRuleMultiResponse

The Security Policy Rule list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[SecurityPolicyRule]**](SecurityPolicyRule.md) | The list of Security Policy Rule objects. | [optional] 

## Example

```python
from fw.models.security_policy_rule_multi_response import SecurityPolicyRuleMultiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPolicyRuleMultiResponse from a JSON string
security_policy_rule_multi_response_instance = SecurityPolicyRuleMultiResponse.from_json(json)
# print the JSON string representation of the object
print(SecurityPolicyRuleMultiResponse.to_json())

# convert the object into a dict
security_policy_rule_multi_response_dict = security_policy_rule_multi_response_instance.to_dict()
# create an instance of SecurityPolicyRuleMultiResponse from a dict
security_policy_rule_multi_response_from_dict = SecurityPolicyRuleMultiResponse.from_dict(security_policy_rule_multi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


