# ListFederatedBlockResponse

The response format to retrieve __FederatedBlock__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[FederatedBlock]**](FederatedBlock.md) | A list of FederatedBlock objects. | [optional] 

## Example

```python
from ipam_federation.models.list_federated_block_response import ListFederatedBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListFederatedBlockResponse from a JSON string
list_federated_block_response_instance = ListFederatedBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ListFederatedBlockResponse.to_json())

# convert the object into a dict
list_federated_block_response_dict = list_federated_block_response_instance.to_dict()
# create an instance of ListFederatedBlockResponse from a dict
list_federated_block_response_from_dict = ListFederatedBlockResponse.from_dict(list_federated_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


