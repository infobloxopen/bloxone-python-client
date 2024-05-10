# NamedListCreateResponse

The Named List create response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**NamedList**](NamedList.md) |  | [optional] 

## Example

```python
from fw.models.named_list_create_response import NamedListCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NamedListCreateResponse from a JSON string
named_list_create_response_instance = NamedListCreateResponse.from_json(json)
# print the JSON string representation of the object
print(NamedListCreateResponse.to_json())

# convert the object into a dict
named_list_create_response_dict = named_list_create_response_instance.to_dict()
# create an instance of NamedListCreateResponse from a dict
named_list_create_response_from_dict = NamedListCreateResponse.from_dict(named_list_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


