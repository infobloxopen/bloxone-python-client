# MacAddressItemUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the resource that was requested to be uploaded. | [optional] 
**hardware_filter_id** | **str** | The resource identifier. | [optional] 
**job_id** | **str** | An Unique Id to identify upload operation. | [optional] 

## Example

```python
from ipam.models.mac_address_item_upload_response import MacAddressItemUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MacAddressItemUploadResponse from a JSON string
mac_address_item_upload_response_instance = MacAddressItemUploadResponse.from_json(json)
# print the JSON string representation of the object
print(MacAddressItemUploadResponse.to_json())

# convert the object into a dict
mac_address_item_upload_response_dict = mac_address_item_upload_response_instance.to_dict()
# create an instance of MacAddressItemUploadResponse from a dict
mac_address_item_upload_response_from_dict = MacAddressItemUploadResponse.from_dict(mac_address_item_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


