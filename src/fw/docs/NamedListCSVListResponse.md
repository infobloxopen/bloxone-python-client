# NamedListCSVListResponse

The Named List CSV list response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[str]** | Named Lists for csv file | [optional] 

## Example

```python
from fw.models.named_list_csv_list_response import NamedListCSVListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NamedListCSVListResponse from a JSON string
named_list_csv_list_response_instance = NamedListCSVListResponse.from_json(json)
# print the JSON string representation of the object
print(NamedListCSVListResponse.to_json())

# convert the object into a dict
named_list_csv_list_response_dict = named_list_csv_list_response_instance.to_dict()
# create an instance of NamedListCSVListResponse from a dict
named_list_csv_list_response_from_dict = NamedListCSVListResponse.from_dict(named_list_csv_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


