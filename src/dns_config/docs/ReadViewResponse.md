# ReadViewResponse

The View object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**View**](View.md) | The View object. | [optional] 

## Example

```python
from dns_config.models.read_view_response import ReadViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadViewResponse from a JSON string
read_view_response_instance = ReadViewResponse.from_json(json)
# print the JSON string representation of the object
print(ReadViewResponse.to_json())

# convert the object into a dict
read_view_response_dict = read_view_response_instance.to_dict()
# create an instance of ReadViewResponse from a dict
read_view_response_from_dict = ReadViewResponse.from_dict(read_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


