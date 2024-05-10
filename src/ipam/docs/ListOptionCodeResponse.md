# ListOptionCodeResponse

The response format to retrieve __OptionCode__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[OptionCode]**](OptionCode.md) | The list of OptionCode objects. | [optional] 

## Example

```python
from ipam.models.list_option_code_response import ListOptionCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOptionCodeResponse from a JSON string
list_option_code_response_instance = ListOptionCodeResponse.from_json(json)
# print the JSON string representation of the object
print(ListOptionCodeResponse.to_json())

# convert the object into a dict
list_option_code_response_dict = list_option_code_response_instance.to_dict()
# create an instance of ListOptionCodeResponse from a dict
list_option_code_response_from_dict = ListOptionCodeResponse.from_dict(list_option_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


