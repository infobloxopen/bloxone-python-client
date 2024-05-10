# ListFilterResponse

The response format to retrieve DHCP __Filter__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Filter]**](Filter.md) | The list of DHCP Filter objects. | [optional] 

## Example

```python
from ipam.models.list_filter_response import ListFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListFilterResponse from a JSON string
list_filter_response_instance = ListFilterResponse.from_json(json)
# print the JSON string representation of the object
print(ListFilterResponse.to_json())

# convert the object into a dict
list_filter_response_dict = list_filter_response_instance.to_dict()
# create an instance of ListFilterResponse from a dict
list_filter_response_from_dict = ListFilterResponse.from_dict(list_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


