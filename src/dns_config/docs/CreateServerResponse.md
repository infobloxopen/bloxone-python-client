# CreateServerResponse

The Server object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Server**](Server.md) |  | [optional] 

## Example

```python
from dns_config.models.create_server_response import CreateServerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServerResponse from a JSON string
create_server_response_instance = CreateServerResponse.from_json(json)
# print the JSON string representation of the object
print(CreateServerResponse.to_json())

# convert the object into a dict
create_server_response_dict = create_server_response_instance.to_dict()
# create an instance of CreateServerResponse from a dict
create_server_response_from_dict = CreateServerResponse.from_dict(create_server_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


