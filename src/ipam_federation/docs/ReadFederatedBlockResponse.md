# ReadFederatedBlockResponse

The response format to retrieve the __FederatedBlock__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**FederatedBlock**](FederatedBlock.md) | The FederatedBlock object. | [optional] 

## Example

```python
from ipam_federation.models.read_federated_block_response import ReadFederatedBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadFederatedBlockResponse from a JSON string
read_federated_block_response_instance = ReadFederatedBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ReadFederatedBlockResponse.to_json())

# convert the object into a dict
read_federated_block_response_dict = read_federated_block_response_instance.to_dict()
# create an instance of ReadFederatedBlockResponse from a dict
read_federated_block_response_from_dict = ReadFederatedBlockResponse.from_dict(read_federated_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


