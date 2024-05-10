# SecurityPoliciesCreateSecurityPolicy400ResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fw.models.security_policies_create_security_policy400_response_error import SecurityPoliciesCreateSecurityPolicy400ResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPoliciesCreateSecurityPolicy400ResponseError from a JSON string
security_policies_create_security_policy400_response_error_instance = SecurityPoliciesCreateSecurityPolicy400ResponseError.from_json(json)
# print the JSON string representation of the object
print(SecurityPoliciesCreateSecurityPolicy400ResponseError.to_json())

# convert the object into a dict
security_policies_create_security_policy400_response_error_dict = security_policies_create_security_policy400_response_error_instance.to_dict()
# create an instance of SecurityPoliciesCreateSecurityPolicy400ResponseError from a dict
security_policies_create_security_policy400_response_error_from_dict = SecurityPoliciesCreateSecurityPolicy400ResponseError.from_dict(security_policies_create_security_policy400_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


