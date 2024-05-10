# CategoryFilterMultiResponse

The Category Filter list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CategoryFilter]**](CategoryFilter.md) | The list of Category Filter objects. | [optional] 

## Example

```python
from fw.models.category_filter_multi_response import CategoryFilterMultiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryFilterMultiResponse from a JSON string
category_filter_multi_response_instance = CategoryFilterMultiResponse.from_json(json)
# print the JSON string representation of the object
print(CategoryFilterMultiResponse.to_json())

# convert the object into a dict
category_filter_multi_response_dict = category_filter_multi_response_instance.to_dict()
# create an instance of CategoryFilterMultiResponse from a dict
category_filter_multi_response_from_dict = CategoryFilterMultiResponse.from_dict(category_filter_multi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


