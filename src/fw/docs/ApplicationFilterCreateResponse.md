# ApplicationFilterCreateResponse

The Application Filter create response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**ApplicationFilter**](ApplicationFilter.md) |  | [optional] 

## Example

```python
from fw.models.application_filter_create_response import ApplicationFilterCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFilterCreateResponse from a JSON string
application_filter_create_response_instance = ApplicationFilterCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationFilterCreateResponse.to_json())

# convert the object into a dict
application_filter_create_response_dict = application_filter_create_response_instance.to_dict()
# create an instance of ApplicationFilterCreateResponse from a dict
application_filter_create_response_from_dict = ApplicationFilterCreateResponse.from_dict(application_filter_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


