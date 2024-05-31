# CategoryFilterReadResponse

The Category Filter read response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**CategoryFilter**](CategoryFilter.md) | The Category Filter object. | [optional] 

## Example

```python
from fw.models.category_filter_read_response import CategoryFilterReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryFilterReadResponse from a JSON string
category_filter_read_response_instance = CategoryFilterReadResponse.from_json(json)
# print the JSON string representation of the object
print(CategoryFilterReadResponse.to_json())

# convert the object into a dict
category_filter_read_response_dict = category_filter_read_response_instance.to_dict()
# create an instance of CategoryFilterReadResponse from a dict
category_filter_read_response_from_dict = CategoryFilterReadResponse.from_dict(category_filter_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


