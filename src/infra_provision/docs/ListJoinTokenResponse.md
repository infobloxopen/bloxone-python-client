# ListJoinTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**ApiPageInfo**](ApiPageInfo.md) |  | [optional] 
**results** | [**List[JoinToken]**](JoinToken.md) |  | [optional] 

## Example

```python
from infra_provision.models.list_join_token_response import ListJoinTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListJoinTokenResponse from a JSON string
list_join_token_response_instance = ListJoinTokenResponse.from_json(json)
# print the JSON string representation of the object
print(ListJoinTokenResponse.to_json())

# convert the object into a dict
list_join_token_response_dict = list_join_token_response_instance.to_dict()
# create an instance of ListJoinTokenResponse from a dict
list_join_token_response_from_dict = ListJoinTokenResponse.from_dict(list_join_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


