# NetworkListsDeleteNetworkLists400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**NetworkListsDeleteNetworkLists400ResponseError**](NetworkListsDeleteNetworkLists400ResponseError.md) |  | [optional] 

## Example

```python
from fw.models.network_lists_delete_network_lists400_response import NetworkListsDeleteNetworkLists400Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkListsDeleteNetworkLists400Response from a JSON string
network_lists_delete_network_lists400_response_instance = NetworkListsDeleteNetworkLists400Response.from_json(json)
# print the JSON string representation of the object
print(NetworkListsDeleteNetworkLists400Response.to_json())

# convert the object into a dict
network_lists_delete_network_lists400_response_dict = network_lists_delete_network_lists400_response_instance.to_dict()
# create an instance of NetworkListsDeleteNetworkLists400Response from a dict
network_lists_delete_network_lists400_response_from_dict = NetworkListsDeleteNetworkLists400Response.from_dict(network_lists_delete_network_lists400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


