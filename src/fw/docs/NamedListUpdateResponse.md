# NamedListUpdateResponse

The Named List update response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**NamedList**](NamedList.md) | The Named List object. | [optional] 

## Example

```python
from fw.models.named_list_update_response import NamedListUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NamedListUpdateResponse from a JSON string
named_list_update_response_instance = NamedListUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(NamedListUpdateResponse.to_json())

# convert the object into a dict
named_list_update_response_dict = named_list_update_response_instance.to_dict()
# create an instance of NamedListUpdateResponse from a dict
named_list_update_response_from_dict = NamedListUpdateResponse.from_dict(named_list_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


