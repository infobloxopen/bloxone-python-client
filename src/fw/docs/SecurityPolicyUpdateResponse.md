# SecurityPolicyUpdateResponse

The Security Policy update response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**SecurityPolicy**](SecurityPolicy.md) |  | [optional] 

## Example

```python
from fw.models.security_policy_update_response import SecurityPolicyUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPolicyUpdateResponse from a JSON string
security_policy_update_response_instance = SecurityPolicyUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(SecurityPolicyUpdateResponse.to_json())

# convert the object into a dict
security_policy_update_response_dict = security_policy_update_response_instance.to_dict()
# create an instance of SecurityPolicyUpdateResponse from a dict
security_policy_update_response_from_dict = SecurityPolicyUpdateResponse.from_dict(security_policy_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


