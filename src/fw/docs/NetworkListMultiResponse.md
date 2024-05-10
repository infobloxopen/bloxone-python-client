# NetworkListMultiResponse

The Network List list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[NetworkList]**](NetworkList.md) | The list of Network List objects. | [optional] 

## Example

```python
from fw.models.network_list_multi_response import NetworkListMultiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkListMultiResponse from a JSON string
network_list_multi_response_instance = NetworkListMultiResponse.from_json(json)
# print the JSON string representation of the object
print(NetworkListMultiResponse.to_json())

# convert the object into a dict
network_list_multi_response_dict = network_list_multi_response_instance.to_dict()
# create an instance of NetworkListMultiResponse from a dict
network_list_multi_response_from_dict = NetworkListMultiResponse.from_dict(network_list_multi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


