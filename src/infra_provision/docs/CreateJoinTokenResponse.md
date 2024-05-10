# CreateJoinTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**join_token** | **str** |  | [optional] 
**result** | [**JoinToken**](JoinToken.md) |  | [optional] 

## Example

```python
from infra_provision.models.create_join_token_response import CreateJoinTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJoinTokenResponse from a JSON string
create_join_token_response_instance = CreateJoinTokenResponse.from_json(json)
# print the JSON string representation of the object
print(CreateJoinTokenResponse.to_json())

# convert the object into a dict
create_join_token_response_dict = create_join_token_response_instance.to_dict()
# create an instance of CreateJoinTokenResponse from a dict
create_join_token_response_from_dict = CreateJoinTokenResponse.from_dict(create_join_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


