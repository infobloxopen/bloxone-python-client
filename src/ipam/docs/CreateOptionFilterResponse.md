# CreateOptionFilterResponse

The response format to create the __OptionFilter__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OptionFilter**](OptionFilter.md) | The created OptionFilter object. | [optional] 

## Example

```python
from ipam.models.create_option_filter_response import CreateOptionFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOptionFilterResponse from a JSON string
create_option_filter_response_instance = CreateOptionFilterResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOptionFilterResponse.to_json())

# convert the object into a dict
create_option_filter_response_dict = create_option_filter_response_instance.to_dict()
# create an instance of CreateOptionFilterResponse from a dict
create_option_filter_response_from_dict = CreateOptionFilterResponse.from_dict(create_option_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


