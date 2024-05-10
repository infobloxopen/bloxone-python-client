# UpdateJoinTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**JoinToken**](JoinToken.md) |  | [optional] 

## Example

```python
from infra_provision.models.update_join_token_response import UpdateJoinTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateJoinTokenResponse from a JSON string
update_join_token_response_instance = UpdateJoinTokenResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateJoinTokenResponse.to_json())

# convert the object into a dict
update_join_token_response_dict = update_join_token_response_instance.to_dict()
# create an instance of UpdateJoinTokenResponse from a dict
update_join_token_response_from_dict = UpdateJoinTokenResponse.from_dict(update_join_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


