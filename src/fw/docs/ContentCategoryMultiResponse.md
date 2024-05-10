# ContentCategoryMultiResponse

The Content Category list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ContentCategory]**](ContentCategory.md) | The list of Content Category objects. | [optional] 

## Example

```python
from fw.models.content_category_multi_response import ContentCategoryMultiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentCategoryMultiResponse from a JSON string
content_category_multi_response_instance = ContentCategoryMultiResponse.from_json(json)
# print the JSON string representation of the object
print(ContentCategoryMultiResponse.to_json())

# convert the object into a dict
content_category_multi_response_dict = content_category_multi_response_instance.to_dict()
# create an instance of ContentCategoryMultiResponse from a dict
content_category_multi_response_from_dict = ContentCategoryMultiResponse.from_dict(content_category_multi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


