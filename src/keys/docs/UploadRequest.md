# UploadRequest

The request format for uploading content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The description for uploaded content. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**content** | **str** | Base64 encoded content. | 
**fields** | [**ProtobufFieldMask**](ProtobufFieldMask.md) |  | [optional] 
**tags** | **object** | The tags for uploaded content in JSON format. | [optional] 
**type** | [**UploadContentType**](UploadContentType.md) | Type of uploaded content. | 

## Example

```python
from keys.models.upload_request import UploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadRequest from a JSON string
upload_request_instance = UploadRequest.from_json(json)
# print the JSON string representation of the object
print(UploadRequest.to_json())

# convert the object into a dict
upload_request_dict = upload_request_instance.to_dict()
# create an instance of UploadRequest from a dict
upload_request_from_dict = UploadRequest.from_dict(upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


