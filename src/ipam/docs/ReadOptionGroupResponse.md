# ReadOptionGroupResponse

The response format to retrieve the __OptionGroup__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OptionGroup**](OptionGroup.md) | The OptionGroup object. | [optional] 

## Example

```python
from ipam.models.read_option_group_response import ReadOptionGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadOptionGroupResponse from a JSON string
read_option_group_response_instance = ReadOptionGroupResponse.from_json(json)
# print the JSON string representation of the object
print(ReadOptionGroupResponse.to_json())

# convert the object into a dict
read_option_group_response_dict = read_option_group_response_instance.to_dict()
# create an instance of ReadOptionGroupResponse from a dict
read_option_group_response_from_dict = ReadOptionGroupResponse.from_dict(read_option_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


