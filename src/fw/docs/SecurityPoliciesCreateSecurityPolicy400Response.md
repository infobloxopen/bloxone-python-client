# SecurityPoliciesCreateSecurityPolicy400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**SecurityPoliciesCreateSecurityPolicy400ResponseError**](SecurityPoliciesCreateSecurityPolicy400ResponseError.md) |  | [optional] 

## Example

```python
from fw.models.security_policies_create_security_policy400_response import SecurityPoliciesCreateSecurityPolicy400Response

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPoliciesCreateSecurityPolicy400Response from a JSON string
security_policies_create_security_policy400_response_instance = SecurityPoliciesCreateSecurityPolicy400Response.from_json(json)
# print the JSON string representation of the object
print(SecurityPoliciesCreateSecurityPolicy400Response.to_json())

# convert the object into a dict
security_policies_create_security_policy400_response_dict = security_policies_create_security_policy400_response_instance.to_dict()
# create an instance of SecurityPoliciesCreateSecurityPolicy400Response from a dict
security_policies_create_security_policy400_response_from_dict = SecurityPoliciesCreateSecurityPolicy400Response.from_dict(security_policies_create_security_policy400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


