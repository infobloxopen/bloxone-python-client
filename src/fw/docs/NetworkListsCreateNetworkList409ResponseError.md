# NetworkListsCreateNetworkList409ResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fw.models.network_lists_create_network_list409_response_error import NetworkListsCreateNetworkList409ResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkListsCreateNetworkList409ResponseError from a JSON string
network_lists_create_network_list409_response_error_instance = NetworkListsCreateNetworkList409ResponseError.from_json(json)
# print the JSON string representation of the object
print(NetworkListsCreateNetworkList409ResponseError.to_json())

# convert the object into a dict
network_lists_create_network_list409_response_error_dict = network_lists_create_network_list409_response_error_instance.to_dict()
# create an instance of NetworkListsCreateNetworkList409ResponseError from a dict
network_lists_create_network_list409_response_error_from_dict = NetworkListsCreateNetworkList409ResponseError.from_dict(network_lists_create_network_list409_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


