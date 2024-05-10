# ApplicationFiltersDeleteRequest

The Application Filter delete request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | The list of Application Filter object identifiers. | [optional] 

## Example

```python
from fw.models.application_filters_delete_request import ApplicationFiltersDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFiltersDeleteRequest from a JSON string
application_filters_delete_request_instance = ApplicationFiltersDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationFiltersDeleteRequest.to_json())

# convert the object into a dict
application_filters_delete_request_dict = application_filters_delete_request_instance.to_dict()
# create an instance of ApplicationFiltersDeleteRequest from a dict
application_filters_delete_request_from_dict = ApplicationFiltersDeleteRequest.from_dict(application_filters_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


