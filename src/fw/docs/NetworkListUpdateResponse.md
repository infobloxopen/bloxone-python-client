# NetworkListUpdateResponse

The Network List update response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**NetworkList**](NetworkList.md) |  | [optional] 

## Example

```python
from fw.models.network_list_update_response import NetworkListUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkListUpdateResponse from a JSON string
network_list_update_response_instance = NetworkListUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(NetworkListUpdateResponse.to_json())

# convert the object into a dict
network_list_update_response_dict = network_list_update_response_instance.to_dict()
# create an instance of NetworkListUpdateResponse from a dict
network_list_update_response_from_dict = NetworkListUpdateResponse.from_dict(network_list_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


