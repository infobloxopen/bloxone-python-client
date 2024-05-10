# ListOptionGroupResponse

The response format to retrieve __OptionGroup__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[OptionGroup]**](OptionGroup.md) | A list of OptionGroup objects. | [optional] 

## Example

```python
from ipam.models.list_option_group_response import ListOptionGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOptionGroupResponse from a JSON string
list_option_group_response_instance = ListOptionGroupResponse.from_json(json)
# print the JSON string representation of the object
print(ListOptionGroupResponse.to_json())

# convert the object into a dict
list_option_group_response_dict = list_option_group_response_instance.to_dict()
# create an instance of ListOptionGroupResponse from a dict
list_option_group_response_from_dict = ListOptionGroupResponse.from_dict(list_option_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


