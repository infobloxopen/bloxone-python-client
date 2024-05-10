# ReadDelegationResponse

The Delegation object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Delegation**](Delegation.md) |  | [optional] 

## Example

```python
from dns_config.models.read_delegation_response import ReadDelegationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadDelegationResponse from a JSON string
read_delegation_response_instance = ReadDelegationResponse.from_json(json)
# print the JSON string representation of the object
print(ReadDelegationResponse.to_json())

# convert the object into a dict
read_delegation_response_dict = read_delegation_response_instance.to_dict()
# create an instance of ReadDelegationResponse from a dict
read_delegation_response_from_dict = ReadDelegationResponse.from_dict(read_delegation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


