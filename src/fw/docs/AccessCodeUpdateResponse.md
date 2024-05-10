# AccessCodeUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**AccessCode**](AccessCode.md) |  | [optional] 

## Example

```python
from fw.models.access_code_update_response import AccessCodeUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessCodeUpdateResponse from a JSON string
access_code_update_response_instance = AccessCodeUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(AccessCodeUpdateResponse.to_json())

# convert the object into a dict
access_code_update_response_dict = access_code_update_response_instance.to_dict()
# create an instance of AccessCodeUpdateResponse from a dict
access_code_update_response_from_dict = AccessCodeUpdateResponse.from_dict(access_code_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


