# SecurityPoliciesReadSecurityPolicy404ResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fw.models.security_policies_read_security_policy404_response_error import SecurityPoliciesReadSecurityPolicy404ResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPoliciesReadSecurityPolicy404ResponseError from a JSON string
security_policies_read_security_policy404_response_error_instance = SecurityPoliciesReadSecurityPolicy404ResponseError.from_json(json)
# print the JSON string representation of the object
print(SecurityPoliciesReadSecurityPolicy404ResponseError.to_json())

# convert the object into a dict
security_policies_read_security_policy404_response_error_dict = security_policies_read_security_policy404_response_error_instance.to_dict()
# create an instance of SecurityPoliciesReadSecurityPolicy404ResponseError from a dict
security_policies_read_security_policy404_response_error_from_dict = SecurityPoliciesReadSecurityPolicy404ResponseError.from_dict(security_policies_read_security_policy404_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


