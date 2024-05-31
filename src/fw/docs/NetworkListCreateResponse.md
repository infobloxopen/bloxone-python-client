# NetworkListCreateResponse

The Network List create response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**NetworkList**](NetworkList.md) | The Network List object. | [optional] 

## Example

```python
from fw.models.network_list_create_response import NetworkListCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkListCreateResponse from a JSON string
network_list_create_response_instance = NetworkListCreateResponse.from_json(json)
# print the JSON string representation of the object
print(NetworkListCreateResponse.to_json())

# convert the object into a dict
network_list_create_response_dict = network_list_create_response_instance.to_dict()
# create an instance of NetworkListCreateResponse from a dict
network_list_create_response_from_dict = NetworkListCreateResponse.from_dict(network_list_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


