# CreateNextAvailableFederatedBlockResponse

The response format to allocate next available __FederatedBlock__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[FederatedBlock]**](FederatedBlock.md) |  | [optional] 

## Example

```python
from ipam_federation.models.create_next_available_federated_block_response import CreateNextAvailableFederatedBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNextAvailableFederatedBlockResponse from a JSON string
create_next_available_federated_block_response_instance = CreateNextAvailableFederatedBlockResponse.from_json(json)
# print the JSON string representation of the object
print(CreateNextAvailableFederatedBlockResponse.to_json())

# convert the object into a dict
create_next_available_federated_block_response_dict = create_next_available_federated_block_response_instance.to_dict()
# create an instance of CreateNextAvailableFederatedBlockResponse from a dict
create_next_available_federated_block_response_from_dict = CreateNextAvailableFederatedBlockResponse.from_dict(create_next_available_federated_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


