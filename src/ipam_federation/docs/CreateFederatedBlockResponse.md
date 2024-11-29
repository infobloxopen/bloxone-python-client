# CreateFederatedBlockResponse

The response format to create the __FederatedBlock__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**FederatedBlock**](FederatedBlock.md) | The created FederatedBlock object. | [optional] 

## Example

```python
from ipam_federation.models.create_federated_block_response import CreateFederatedBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFederatedBlockResponse from a JSON string
create_federated_block_response_instance = CreateFederatedBlockResponse.from_json(json)
# print the JSON string representation of the object
print(CreateFederatedBlockResponse.to_json())

# convert the object into a dict
create_federated_block_response_dict = create_federated_block_response_instance.to_dict()
# create an instance of CreateFederatedBlockResponse from a dict
create_federated_block_response_from_dict = CreateFederatedBlockResponse.from_dict(create_federated_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


