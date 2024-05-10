# SecurityPoliciesCreateSecurityPolicy409ResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fw.models.security_policies_create_security_policy409_response_error import SecurityPoliciesCreateSecurityPolicy409ResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPoliciesCreateSecurityPolicy409ResponseError from a JSON string
security_policies_create_security_policy409_response_error_instance = SecurityPoliciesCreateSecurityPolicy409ResponseError.from_json(json)
# print the JSON string representation of the object
print(SecurityPoliciesCreateSecurityPolicy409ResponseError.to_json())

# convert the object into a dict
security_policies_create_security_policy409_response_error_dict = security_policies_create_security_policy409_response_error_instance.to_dict()
# create an instance of SecurityPoliciesCreateSecurityPolicy409ResponseError from a dict
security_policies_create_security_policy409_response_error_from_dict = SecurityPoliciesCreateSecurityPolicy409ResponseError.from_dict(security_policies_create_security_policy409_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


