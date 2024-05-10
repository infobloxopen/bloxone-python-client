# DeleteJoinTokensRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The resource identifier. | [optional] 

## Example

```python
from infra_provision.models.delete_join_tokens_request import DeleteJoinTokensRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteJoinTokensRequest from a JSON string
delete_join_tokens_request_instance = DeleteJoinTokensRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteJoinTokensRequest.to_json())

# convert the object into a dict
delete_join_tokens_request_dict = delete_join_tokens_request_instance.to_dict()
# create an instance of DeleteJoinTokensRequest from a dict
delete_join_tokens_request_from_dict = DeleteJoinTokensRequest.from_dict(delete_join_tokens_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


