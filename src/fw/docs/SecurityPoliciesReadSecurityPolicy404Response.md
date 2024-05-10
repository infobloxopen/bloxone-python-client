# SecurityPoliciesReadSecurityPolicy404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**SecurityPoliciesReadSecurityPolicy404ResponseError**](SecurityPoliciesReadSecurityPolicy404ResponseError.md) |  | [optional] 

## Example

```python
from fw.models.security_policies_read_security_policy404_response import SecurityPoliciesReadSecurityPolicy404Response

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPoliciesReadSecurityPolicy404Response from a JSON string
security_policies_read_security_policy404_response_instance = SecurityPoliciesReadSecurityPolicy404Response.from_json(json)
# print the JSON string representation of the object
print(SecurityPoliciesReadSecurityPolicy404Response.to_json())

# convert the object into a dict
security_policies_read_security_policy404_response_dict = security_policies_read_security_policy404_response_instance.to_dict()
# create an instance of SecurityPoliciesReadSecurityPolicy404Response from a dict
security_policies_read_security_policy404_response_from_dict = SecurityPoliciesReadSecurityPolicy404Response.from_dict(security_policies_read_security_policy404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


