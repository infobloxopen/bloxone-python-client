# ReadJoinTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**JoinToken**](JoinToken.md) |  | [optional] 

## Example

```python
from infra_provision.models.read_join_token_response import ReadJoinTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadJoinTokenResponse from a JSON string
read_join_token_response_instance = ReadJoinTokenResponse.from_json(json)
# print the JSON string representation of the object
print(ReadJoinTokenResponse.to_json())

# convert the object into a dict
read_join_token_response_dict = read_join_token_response_instance.to_dict()
# create an instance of ReadJoinTokenResponse from a dict
read_join_token_response_from_dict = ReadJoinTokenResponse.from_dict(read_join_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


