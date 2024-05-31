# UpdateOptionFilterResponse

The response format to update the __OptionFilter__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OptionFilter**](OptionFilter.md) | The OptionFilter object. | [optional] 

## Example

```python
from ipam.models.update_option_filter_response import UpdateOptionFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOptionFilterResponse from a JSON string
update_option_filter_response_instance = UpdateOptionFilterResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateOptionFilterResponse.to_json())

# convert the object into a dict
update_option_filter_response_dict = update_option_filter_response_instance.to_dict()
# create an instance of UpdateOptionFilterResponse from a dict
update_option_filter_response_from_dict = UpdateOptionFilterResponse.from_dict(update_option_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


