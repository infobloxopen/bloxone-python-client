# CreateDelegationResponse

The Delegation object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Delegation**](Delegation.md) |  | [optional] 

## Example

```python
from dns_config.models.create_delegation_response import CreateDelegationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDelegationResponse from a JSON string
create_delegation_response_instance = CreateDelegationResponse.from_json(json)
# print the JSON string representation of the object
print(CreateDelegationResponse.to_json())

# convert the object into a dict
create_delegation_response_dict = create_delegation_response_instance.to_dict()
# create an instance of CreateDelegationResponse from a dict
create_delegation_response_from_dict = CreateDelegationResponse.from_dict(create_delegation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


