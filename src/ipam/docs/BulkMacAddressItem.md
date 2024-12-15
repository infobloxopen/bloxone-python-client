# BulkMacAddressItem

A __BulkMacAddressItem__ object creates mac address items in bulk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | The addresses to match for the hardware filter. | 
**hardware_filter_id** | **str** | The resource identifier. | 

## Example

```python
from ipam.models.bulk_mac_address_item import BulkMacAddressItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkMacAddressItem from a JSON string
bulk_mac_address_item_instance = BulkMacAddressItem.from_json(json)
# print the JSON string representation of the object
print(BulkMacAddressItem.to_json())

# convert the object into a dict
bulk_mac_address_item_dict = bulk_mac_address_item_instance.to_dict()
# create an instance of BulkMacAddressItem from a dict
bulk_mac_address_item_from_dict = BulkMacAddressItem.from_dict(bulk_mac_address_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


