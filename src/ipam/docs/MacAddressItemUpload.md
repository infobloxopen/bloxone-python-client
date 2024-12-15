# MacAddressItemUpload

A __MacAddressItemUpload__ object uploads mac addresses to a large scale hardware filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**append** | **bool** | If data needs to be appended or overwritten. Defaults to _true_. | [optional] 
**content** | **str** | The content in plain text of the mac addresses to be uploaded to a large scale hardware filter. | 
**hardware_filter_id** | **str** | The resource identifier. | 

## Example

```python
from ipam.models.mac_address_item_upload import MacAddressItemUpload

# TODO update the JSON string below
json = "{}"
# create an instance of MacAddressItemUpload from a JSON string
mac_address_item_upload_instance = MacAddressItemUpload.from_json(json)
# print the JSON string representation of the object
print(MacAddressItemUpload.to_json())

# convert the object into a dict
mac_address_item_upload_dict = mac_address_item_upload_instance.to_dict()
# create an instance of MacAddressItemUpload from a dict
mac_address_item_upload_from_dict = MacAddressItemUpload.from_dict(mac_address_item_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


