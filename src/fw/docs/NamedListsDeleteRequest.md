# NamedListsDeleteRequest

The Named List delete request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | The list of Named List object identifiers. | [optional] 

## Example

```python
from fw.models.named_lists_delete_request import NamedListsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NamedListsDeleteRequest from a JSON string
named_lists_delete_request_instance = NamedListsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(NamedListsDeleteRequest.to_json())

# convert the object into a dict
named_lists_delete_request_dict = named_lists_delete_request_instance.to_dict()
# create an instance of NamedListsDeleteRequest from a dict
named_lists_delete_request_from_dict = NamedListsDeleteRequest.from_dict(named_lists_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


