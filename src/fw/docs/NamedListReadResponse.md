# NamedListReadResponse

The Named List read response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**NamedList**](NamedList.md) | The Named List object. | [optional] 

## Example

```python
from fw.models.named_list_read_response import NamedListReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NamedListReadResponse from a JSON string
named_list_read_response_instance = NamedListReadResponse.from_json(json)
# print the JSON string representation of the object
print(NamedListReadResponse.to_json())

# convert the object into a dict
named_list_read_response_dict = named_list_read_response_instance.to_dict()
# create an instance of NamedListReadResponse from a dict
named_list_read_response_from_dict = NamedListReadResponse.from_dict(named_list_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


