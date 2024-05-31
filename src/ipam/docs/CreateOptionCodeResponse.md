# CreateOptionCodeResponse

The response format to create the __OptionCode__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OptionCode**](OptionCode.md) | The created OptionCode object. | [optional] 

## Example

```python
from ipam.models.create_option_code_response import CreateOptionCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOptionCodeResponse from a JSON string
create_option_code_response_instance = CreateOptionCodeResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOptionCodeResponse.to_json())

# convert the object into a dict
create_option_code_response_dict = create_option_code_response_instance.to_dict()
# create an instance of CreateOptionCodeResponse from a dict
create_option_code_response_from_dict = CreateOptionCodeResponse.from_dict(create_option_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


