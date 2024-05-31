# UpdateServerResponse

The Server object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Server**](Server.md) | The Server object. | [optional] 

## Example

```python
from dns_config.models.update_server_response import UpdateServerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServerResponse from a JSON string
update_server_response_instance = UpdateServerResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateServerResponse.to_json())

# convert the object into a dict
update_server_response_dict = update_server_response_instance.to_dict()
# create an instance of UpdateServerResponse from a dict
update_server_response_from_dict = UpdateServerResponse.from_dict(update_server_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


