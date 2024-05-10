# CreateOptionSpaceResponse

The response format to create the __OptionSpace__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OptionSpace**](OptionSpace.md) |  | [optional] 

## Example

```python
from ipam.models.create_option_space_response import CreateOptionSpaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOptionSpaceResponse from a JSON string
create_option_space_response_instance = CreateOptionSpaceResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOptionSpaceResponse.to_json())

# convert the object into a dict
create_option_space_response_dict = create_option_space_response_instance.to_dict()
# create an instance of CreateOptionSpaceResponse from a dict
create_option_space_response_from_dict = CreateOptionSpaceResponse.from_dict(create_option_space_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


