# AccessCodeReadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**AccessCode**](AccessCode.md) |  | [optional] 

## Example

```python
from fw.models.access_code_read_response import AccessCodeReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessCodeReadResponse from a JSON string
access_code_read_response_instance = AccessCodeReadResponse.from_json(json)
# print the JSON string representation of the object
print(AccessCodeReadResponse.to_json())

# convert the object into a dict
access_code_read_response_dict = access_code_read_response_instance.to_dict()
# create an instance of AccessCodeReadResponse from a dict
access_code_read_response_from_dict = AccessCodeReadResponse.from_dict(access_code_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


