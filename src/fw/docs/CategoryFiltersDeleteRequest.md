# CategoryFiltersDeleteRequest

The Category Filter delete request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | The list of Category Filter object identifiers. | [optional] 

## Example

```python
from fw.models.category_filters_delete_request import CategoryFiltersDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryFiltersDeleteRequest from a JSON string
category_filters_delete_request_instance = CategoryFiltersDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(CategoryFiltersDeleteRequest.to_json())

# convert the object into a dict
category_filters_delete_request_dict = category_filters_delete_request_instance.to_dict()
# create an instance of CategoryFiltersDeleteRequest from a dict
category_filters_delete_request_from_dict = CategoryFiltersDeleteRequest.from_dict(category_filters_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


