# CreateServerResponse

The response format to create the __Server__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Server**](Server.md) | The created Server object. | [optional] 

## Example

```python
from ipam.models.create_server_response import CreateServerResponse

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


