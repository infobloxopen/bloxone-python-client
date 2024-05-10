# SecurityPoliciesCreateSecurityPolicy409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**SecurityPoliciesCreateSecurityPolicy409ResponseError**](SecurityPoliciesCreateSecurityPolicy409ResponseError.md) |  | [optional] 

## Example

```python
from fw.models.security_policies_create_security_policy409_response import SecurityPoliciesCreateSecurityPolicy409Response

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPoliciesCreateSecurityPolicy409Response from a JSON string
security_policies_create_security_policy409_response_instance = SecurityPoliciesCreateSecurityPolicy409Response.from_json(json)
# print the JSON string representation of the object
print(SecurityPoliciesCreateSecurityPolicy409Response.to_json())

# convert the object into a dict
security_policies_create_security_policy409_response_dict = security_policies_create_security_policy409_response_instance.to_dict()
# create an instance of SecurityPoliciesCreateSecurityPolicy409Response from a dict
security_policies_create_security_policy409_response_from_dict = SecurityPoliciesCreateSecurityPolicy409Response.from_dict(security_policies_create_security_policy409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


