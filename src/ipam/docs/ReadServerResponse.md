# ReadServerResponse

The response format to retrieve the __Server__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Server**](Server.md) | The Server object. | [optional] 

## Example

```python
from ipam.models.read_server_response import ReadServerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadServerResponse from a JSON string
read_server_response_instance = ReadServerResponse.from_json(json)
# print the JSON string representation of the object
print(ReadServerResponse.to_json())

# convert the object into a dict
read_server_response_dict = read_server_response_instance.to_dict()
# create an instance of ReadServerResponse from a dict
read_server_response_from_dict = ReadServerResponse.from_dict(read_server_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


