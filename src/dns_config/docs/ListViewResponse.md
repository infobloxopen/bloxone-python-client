# ListViewResponse

The View object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[View]**](View.md) | List of View objects. | [optional] 

## Example

```python
from dns_config.models.list_view_response import ListViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListViewResponse from a JSON string
list_view_response_instance = ListViewResponse.from_json(json)
# print the JSON string representation of the object
print(ListViewResponse.to_json())

# convert the object into a dict
list_view_response_dict = list_view_response_instance.to_dict()
# create an instance of ListViewResponse from a dict
list_view_response_from_dict = ListViewResponse.from_dict(list_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


