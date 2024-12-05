# UpdateMacAddressItemResponse

The response format to update the __MacAddressItem__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**MacAddressItem**](MacAddressItem.md) | The __MacAddressItem__ object. | [optional] 

## Example

```python
from ipam.models.update_mac_address_item_response import UpdateMacAddressItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMacAddressItemResponse from a JSON string
update_mac_address_item_response_instance = UpdateMacAddressItemResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateMacAddressItemResponse.to_json())

# convert the object into a dict
update_mac_address_item_response_dict = update_mac_address_item_response_instance.to_dict()
# create an instance of UpdateMacAddressItemResponse from a dict
update_mac_address_item_response_from_dict = UpdateMacAddressItemResponse.from_dict(update_mac_address_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


