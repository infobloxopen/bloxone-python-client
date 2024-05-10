# NetworkListsCreateNetworkList409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**NetworkListsCreateNetworkList409ResponseError**](NetworkListsCreateNetworkList409ResponseError.md) |  | [optional] 

## Example

```python
from fw.models.network_lists_create_network_list409_response import NetworkListsCreateNetworkList409Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkListsCreateNetworkList409Response from a JSON string
network_lists_create_network_list409_response_instance = NetworkListsCreateNetworkList409Response.from_json(json)
# print the JSON string representation of the object
print(NetworkListsCreateNetworkList409Response.to_json())

# convert the object into a dict
network_lists_create_network_list409_response_dict = network_lists_create_network_list409_response_instance.to_dict()
# create an instance of NetworkListsCreateNetworkList409Response from a dict
network_lists_create_network_list409_response_from_dict = NetworkListsCreateNetworkList409Response.from_dict(network_lists_create_network_list409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


