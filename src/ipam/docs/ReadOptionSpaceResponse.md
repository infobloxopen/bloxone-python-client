# ReadOptionSpaceResponse

The response format to retrieve the __OptionSpace__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OptionSpace**](OptionSpace.md) |  | [optional] 

## Example

```python
from ipam.models.read_option_space_response import ReadOptionSpaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadOptionSpaceResponse from a JSON string
read_option_space_response_instance = ReadOptionSpaceResponse.from_json(json)
# print the JSON string representation of the object
print(ReadOptionSpaceResponse.to_json())

# convert the object into a dict
read_option_space_response_dict = read_option_space_response_instance.to_dict()
# create an instance of ReadOptionSpaceResponse from a dict
read_option_space_response_from_dict = ReadOptionSpaceResponse.from_dict(read_option_space_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


