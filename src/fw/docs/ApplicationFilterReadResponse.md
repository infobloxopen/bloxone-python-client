# ApplicationFilterReadResponse

The Application Filter read response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**ApplicationFilter**](ApplicationFilter.md) |  | [optional] 

## Example

```python
from fw.models.application_filter_read_response import ApplicationFilterReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFilterReadResponse from a JSON string
application_filter_read_response_instance = ApplicationFilterReadResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationFilterReadResponse.to_json())

# convert the object into a dict
application_filter_read_response_dict = application_filter_read_response_instance.to_dict()
# create an instance of ApplicationFilterReadResponse from a dict
application_filter_read_response_from_dict = ApplicationFilterReadResponse.from_dict(application_filter_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


