# ListOptionFilterResponse

The response format to retrieve __OptionFilter__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[OptionFilter]**](OptionFilter.md) | The list of OptionFilter objects. | [optional] 

## Example

```python
from ipam.models.list_option_filter_response import ListOptionFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOptionFilterResponse from a JSON string
list_option_filter_response_instance = ListOptionFilterResponse.from_json(json)
# print the JSON string representation of the object
print(ListOptionFilterResponse.to_json())

# convert the object into a dict
list_option_filter_response_dict = list_option_filter_response_instance.to_dict()
# create an instance of ListOptionFilterResponse from a dict
list_option_filter_response_from_dict = ListOptionFilterResponse.from_dict(list_option_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


