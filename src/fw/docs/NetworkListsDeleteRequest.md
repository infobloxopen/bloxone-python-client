# NetworkListsDeleteRequest

The Network List delete request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | The list of Network List object identifiers. | [optional] 

## Example

```python
from fw.models.network_lists_delete_request import NetworkListsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkListsDeleteRequest from a JSON string
network_lists_delete_request_instance = NetworkListsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(NetworkListsDeleteRequest.to_json())

# convert the object into a dict
network_lists_delete_request_dict = network_lists_delete_request_instance.to_dict()
# create an instance of NetworkListsDeleteRequest from a dict
network_lists_delete_request_from_dict = NetworkListsDeleteRequest.from_dict(network_lists_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


