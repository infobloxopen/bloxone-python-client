# DdiuploadResponse

The response format for uploading content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kerberos_keys** | [**KerberosKeys**](KerberosKeys.md) |  | [optional] 
**warning** | **str** | May contain any non-critical warning messages after processing the content. | [optional] 

## Example

```python
from keys.models.ddiupload_response import DdiuploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DdiuploadResponse from a JSON string
ddiupload_response_instance = DdiuploadResponse.from_json(json)
# print the JSON string representation of the object
print(DdiuploadResponse.to_json())

# convert the object into a dict
ddiupload_response_dict = ddiupload_response_instance.to_dict()
# create an instance of DdiuploadResponse from a dict
ddiupload_response_from_dict = DdiuploadResponse.from_dict(ddiupload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


