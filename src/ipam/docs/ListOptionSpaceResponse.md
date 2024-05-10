# ListOptionSpaceResponse

The response format to retrieve __OptionSpace__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[OptionSpace]**](OptionSpace.md) | The list of OptionSpace objects. | [optional] 

## Example

```python
from ipam.models.list_option_space_response import ListOptionSpaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOptionSpaceResponse from a JSON string
list_option_space_response_instance = ListOptionSpaceResponse.from_json(json)
# print the JSON string representation of the object
print(ListOptionSpaceResponse.to_json())

# convert the object into a dict
list_option_space_response_dict = list_option_space_response_instance.to_dict()
# create an instance of ListOptionSpaceResponse from a dict
list_option_space_response_from_dict = ListOptionSpaceResponse.from_dict(list_option_space_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


