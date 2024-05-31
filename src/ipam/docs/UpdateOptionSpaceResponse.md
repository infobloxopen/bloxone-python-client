# UpdateOptionSpaceResponse

The response format to update the __OptionSpace__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OptionSpace**](OptionSpace.md) | The OptionSpace object. | [optional] 

## Example

```python
from ipam.models.update_option_space_response import UpdateOptionSpaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOptionSpaceResponse from a JSON string
update_option_space_response_instance = UpdateOptionSpaceResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateOptionSpaceResponse.to_json())

# convert the object into a dict
update_option_space_response_dict = update_option_space_response_instance.to_dict()
# create an instance of UpdateOptionSpaceResponse from a dict
update_option_space_response_from_dict = UpdateOptionSpaceResponse.from_dict(update_option_space_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


