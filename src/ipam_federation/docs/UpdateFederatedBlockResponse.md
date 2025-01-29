# UpdateFederatedBlockResponse

The response format to update the __FederatedBlock__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**FederatedBlock**](FederatedBlock.md) | The FederatedBlock object. | [optional] 

## Example

```python
from ipam_federation.models.update_federated_block_response import UpdateFederatedBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFederatedBlockResponse from a JSON string
update_federated_block_response_instance = UpdateFederatedBlockResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateFederatedBlockResponse.to_json())

# convert the object into a dict
update_federated_block_response_dict = update_federated_block_response_instance.to_dict()
# create an instance of UpdateFederatedBlockResponse from a dict
update_federated_block_response_from_dict = UpdateFederatedBlockResponse.from_dict(update_federated_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


