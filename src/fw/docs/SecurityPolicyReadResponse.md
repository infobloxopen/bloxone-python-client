# SecurityPolicyReadResponse

The Security Policy read response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**SecurityPolicy**](SecurityPolicy.md) | The Security Policy object. | [optional] 

## Example

```python
from fw.models.security_policy_read_response import SecurityPolicyReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPolicyReadResponse from a JSON string
security_policy_read_response_instance = SecurityPolicyReadResponse.from_json(json)
# print the JSON string representation of the object
print(SecurityPolicyReadResponse.to_json())

# convert the object into a dict
security_policy_read_response_dict = security_policy_read_response_instance.to_dict()
# create an instance of SecurityPolicyReadResponse from a dict
security_policy_read_response_from_dict = SecurityPolicyReadResponse.from_dict(security_policy_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


