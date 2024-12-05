# BulkCreateMacAddressItemResponse

The response format to bulk create the __MacAddressItem__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[MacAddressItem]**](MacAddressItem.md) | The created __MacAddressItem__ objects. | [optional] 

## Example

```python
from ipam.models.bulk_create_mac_address_item_response import BulkCreateMacAddressItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateMacAddressItemResponse from a JSON string
bulk_create_mac_address_item_response_instance = BulkCreateMacAddressItemResponse.from_json(json)
# print the JSON string representation of the object
print(BulkCreateMacAddressItemResponse.to_json())

# convert the object into a dict
bulk_create_mac_address_item_response_dict = bulk_create_mac_address_item_response_instance.to_dict()
# create an instance of BulkCreateMacAddressItemResponse from a dict
bulk_create_mac_address_item_response_from_dict = BulkCreateMacAddressItemResponse.from_dict(bulk_create_mac_address_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


