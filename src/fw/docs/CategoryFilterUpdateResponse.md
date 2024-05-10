# CategoryFilterUpdateResponse

The Category Filter update response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**CategoryFilter**](CategoryFilter.md) |  | [optional] 

## Example

```python
from fw.models.category_filter_update_response import CategoryFilterUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryFilterUpdateResponse from a JSON string
category_filter_update_response_instance = CategoryFilterUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(CategoryFilterUpdateResponse.to_json())

# convert the object into a dict
category_filter_update_response_dict = category_filter_update_response_instance.to_dict()
# create an instance of CategoryFilterUpdateResponse from a dict
category_filter_update_response_from_dict = CategoryFilterUpdateResponse.from_dict(category_filter_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


