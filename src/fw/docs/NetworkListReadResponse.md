# NetworkListReadResponse

The Network List read response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**NetworkList**](NetworkList.md) |  | [optional] 

## Example

```python
from fw.models.network_list_read_response import NetworkListReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkListReadResponse from a JSON string
network_list_read_response_instance = NetworkListReadResponse.from_json(json)
# print the JSON string representation of the object
print(NetworkListReadResponse.to_json())

# convert the object into a dict
network_list_read_response_dict = network_list_read_response_instance.to_dict()
# create an instance of NetworkListReadResponse from a dict
network_list_read_response_from_dict = NetworkListReadResponse.from_dict(network_list_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


