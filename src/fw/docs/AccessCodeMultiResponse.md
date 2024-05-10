# AccessCodeMultiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AccessCode]**](AccessCode.md) | The list of Bypass Code objects. | [optional] 

## Example

```python
from fw.models.access_code_multi_response import AccessCodeMultiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessCodeMultiResponse from a JSON string
access_code_multi_response_instance = AccessCodeMultiResponse.from_json(json)
# print the JSON string representation of the object
print(AccessCodeMultiResponse.to_json())

# convert the object into a dict
access_code_multi_response_dict = access_code_multi_response_instance.to_dict()
# create an instance of AccessCodeMultiResponse from a dict
access_code_multi_response_from_dict = AccessCodeMultiResponse.from_dict(access_code_multi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


