# NamedListsCreateNamedList409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**NamedListsCreateNamedList409ResponseError**](NamedListsCreateNamedList409ResponseError.md) |  | [optional] 

## Example

```python
from fw.models.named_lists_create_named_list409_response import NamedListsCreateNamedList409Response

# TODO update the JSON string below
json = "{}"
# create an instance of NamedListsCreateNamedList409Response from a JSON string
named_lists_create_named_list409_response_instance = NamedListsCreateNamedList409Response.from_json(json)
# print the JSON string representation of the object
print(NamedListsCreateNamedList409Response.to_json())

# convert the object into a dict
named_lists_create_named_list409_response_dict = named_lists_create_named_list409_response_instance.to_dict()
# create an instance of NamedListsCreateNamedList409Response from a dict
named_lists_create_named_list409_response_from_dict = NamedListsCreateNamedList409Response.from_dict(named_lists_create_named_list409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


