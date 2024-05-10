# ListServerResponse

The Server object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Server]**](Server.md) | List of Server objects. | [optional] 

## Example

```python
from dns_config.models.list_server_response import ListServerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListServerResponse from a JSON string
list_server_response_instance = ListServerResponse.from_json(json)
# print the JSON string representation of the object
print(ListServerResponse.to_json())

# convert the object into a dict
list_server_response_dict = list_server_response_instance.to_dict()
# create an instance of ListServerResponse from a dict
list_server_response_from_dict = ListServerResponse.from_dict(list_server_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


