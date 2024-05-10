# ApplicationFilterUpdateResponse

The Application Filter update response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**ApplicationFilter**](ApplicationFilter.md) |  | [optional] 

## Example

```python
from fw.models.application_filter_update_response import ApplicationFilterUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFilterUpdateResponse from a JSON string
application_filter_update_response_instance = ApplicationFilterUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationFilterUpdateResponse.to_json())

# convert the object into a dict
application_filter_update_response_dict = application_filter_update_response_instance.to_dict()
# create an instance of ApplicationFilterUpdateResponse from a dict
application_filter_update_response_from_dict = ApplicationFilterUpdateResponse.from_dict(application_filter_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


