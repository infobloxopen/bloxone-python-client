# AccessCodesCreateAccessCode400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**AccessCodesCreateAccessCode400ResponseError**](AccessCodesCreateAccessCode400ResponseError.md) |  | [optional] 

## Example

```python
from fw.models.access_codes_create_access_code400_response import AccessCodesCreateAccessCode400Response

# TODO update the JSON string below
json = "{}"
# create an instance of AccessCodesCreateAccessCode400Response from a JSON string
access_codes_create_access_code400_response_instance = AccessCodesCreateAccessCode400Response.from_json(json)
# print the JSON string representation of the object
print(AccessCodesCreateAccessCode400Response.to_json())

# convert the object into a dict
access_codes_create_access_code400_response_dict = access_codes_create_access_code400_response_instance.to_dict()
# create an instance of AccessCodesCreateAccessCode400Response from a dict
access_codes_create_access_code400_response_from_dict = AccessCodesCreateAccessCode400Response.from_dict(access_codes_create_access_code400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


