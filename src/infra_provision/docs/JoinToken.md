# JoinToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_at** | **datetime** |  | [optional] [readonly] 
**description** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**last_used_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**status** | [**JoinTokenJoinTokenStatus**](JoinTokenJoinTokenStatus.md) |  | [optional] 
**tags** | **object** |  | [optional] 
**token_id** | **str** | first half of the token. | [optional] [readonly] 
**use_counter** | **int** |  | [optional] [readonly] 

## Example

```python
from infra_provision.models.join_token import JoinToken

# TODO update the JSON string below
json = "{}"
# create an instance of JoinToken from a JSON string
join_token_instance = JoinToken.from_json(json)
# print the JSON string representation of the object
print(JoinToken.to_json())

# convert the object into a dict
join_token_dict = join_token_instance.to_dict()
# create an instance of JoinToken from a dict
join_token_from_dict = JoinToken.from_dict(join_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


