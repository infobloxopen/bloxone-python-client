# CreateOptionGroupResponse

The response format to create the __OptionGroup__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OptionGroup**](OptionGroup.md) |  | [optional] 

## Example

```python
from ipam.models.create_option_group_response import CreateOptionGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOptionGroupResponse from a JSON string
create_option_group_response_instance = CreateOptionGroupResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOptionGroupResponse.to_json())

# convert the object into a dict
create_option_group_response_dict = create_option_group_response_instance.to_dict()
# create an instance of CreateOptionGroupResponse from a dict
create_option_group_response_from_dict = CreateOptionGroupResponse.from_dict(create_option_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


