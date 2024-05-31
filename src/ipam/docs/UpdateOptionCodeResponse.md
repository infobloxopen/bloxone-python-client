# UpdateOptionCodeResponse

The response format to update the __OptionCode__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OptionCode**](OptionCode.md) | The OptionCode object. | [optional] 

## Example

```python
from ipam.models.update_option_code_response import UpdateOptionCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOptionCodeResponse from a JSON string
update_option_code_response_instance = UpdateOptionCodeResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateOptionCodeResponse.to_json())

# convert the object into a dict
update_option_code_response_dict = update_option_code_response_instance.to_dict()
# create an instance of UpdateOptionCodeResponse from a dict
update_option_code_response_from_dict = UpdateOptionCodeResponse.from_dict(update_option_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


