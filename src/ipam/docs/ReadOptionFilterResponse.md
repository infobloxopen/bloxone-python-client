# ReadOptionFilterResponse

The response format to retrieve the __OptionFilter__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**OptionFilter**](OptionFilter.md) | The OptionFilter object. | [optional] 

## Example

```python
from ipam.models.read_option_filter_response import ReadOptionFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadOptionFilterResponse from a JSON string
read_option_filter_response_instance = ReadOptionFilterResponse.from_json(json)
# print the JSON string representation of the object
print(ReadOptionFilterResponse.to_json())

# convert the object into a dict
read_option_filter_response_dict = read_option_filter_response_instance.to_dict()
# create an instance of ReadOptionFilterResponse from a dict
read_option_filter_response_from_dict = ReadOptionFilterResponse.from_dict(read_option_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


