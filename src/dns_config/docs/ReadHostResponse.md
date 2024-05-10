# ReadHostResponse

The DNS Host object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Host**](Host.md) |  | [optional] 

## Example

```python
from dns_config.models.read_host_response import ReadHostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadHostResponse from a JSON string
read_host_response_instance = ReadHostResponse.from_json(json)
# print the JSON string representation of the object
print(ReadHostResponse.to_json())

# convert the object into a dict
read_host_response_dict = read_host_response_instance.to_dict()
# create an instance of ReadHostResponse from a dict
read_host_response_from_dict = ReadHostResponse.from_dict(read_host_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


