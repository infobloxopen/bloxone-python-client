# UpdateDelegationResponse

The Delegation object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Delegation**](Delegation.md) | The updated Delegation object. | [optional] 

## Example

```python
from dns_config.models.update_delegation_response import UpdateDelegationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDelegationResponse from a JSON string
update_delegation_response_instance = UpdateDelegationResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateDelegationResponse.to_json())

# convert the object into a dict
update_delegation_response_dict = update_delegation_response_instance.to_dict()
# create an instance of UpdateDelegationResponse from a dict
update_delegation_response_from_dict = UpdateDelegationResponse.from_dict(update_delegation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


