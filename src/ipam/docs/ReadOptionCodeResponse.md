# ReadOptionCodeResponse

The response format to retrieve the __OptionCode__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OptionCode**](OptionCode.md) | The OptionCode object. | [optional] 

## Example

```python
from ipam.models.read_option_code_response import ReadOptionCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadOptionCodeResponse from a JSON string
read_option_code_response_instance = ReadOptionCodeResponse.from_json(json)
# print the JSON string representation of the object
print(ReadOptionCodeResponse.to_json())

# convert the object into a dict
read_option_code_response_dict = read_option_code_response_instance.to_dict()
# create an instance of ReadOptionCodeResponse from a dict
read_option_code_response_from_dict = ReadOptionCodeResponse.from_dict(read_option_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


