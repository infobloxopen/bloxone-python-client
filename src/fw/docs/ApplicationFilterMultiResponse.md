# ApplicationFilterMultiResponse

The Application Filter list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ApplicationFilter]**](ApplicationFilter.md) | The list of Application Filter objects. | [optional] 

## Example

```python
from fw.models.application_filter_multi_response import ApplicationFilterMultiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFilterMultiResponse from a JSON string
application_filter_multi_response_instance = ApplicationFilterMultiResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationFilterMultiResponse.to_json())

# convert the object into a dict
application_filter_multi_response_dict = application_filter_multi_response_instance.to_dict()
# create an instance of ApplicationFilterMultiResponse from a dict
application_filter_multi_response_from_dict = ApplicationFilterMultiResponse.from_dict(application_filter_multi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


