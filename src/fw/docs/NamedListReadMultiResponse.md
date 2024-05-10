# NamedListReadMultiResponse

The Named List list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[NamedListRead]**](NamedListRead.md) | The list of Named List objects. | [optional] 

## Example

```python
from fw.models.named_list_read_multi_response import NamedListReadMultiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NamedListReadMultiResponse from a JSON string
named_list_read_multi_response_instance = NamedListReadMultiResponse.from_json(json)
# print the JSON string representation of the object
print(NamedListReadMultiResponse.to_json())

# convert the object into a dict
named_list_read_multi_response_dict = named_list_read_multi_response_instance.to_dict()
# create an instance of NamedListReadMultiResponse from a dict
named_list_read_multi_response_from_dict = NamedListReadMultiResponse.from_dict(named_list_read_multi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


