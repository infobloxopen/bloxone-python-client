# MacAddressItem

A __MacAddressItem__ object (_dhcp/mac_address_item_) represents a mac address item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address to match for the hardware filter. | 
**hardware_filter_id** | **str** | The resource identifier. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 

## Example

```python
from ipam.models.mac_address_item import MacAddressItem

# TODO update the JSON string below
json = "{}"
# create an instance of MacAddressItem from a JSON string
mac_address_item_instance = MacAddressItem.from_json(json)
# print the JSON string representation of the object
print(MacAddressItem.to_json())

# convert the object into a dict
mac_address_item_dict = mac_address_item_instance.to_dict()
# create an instance of MacAddressItem from a dict
mac_address_item_from_dict = MacAddressItem.from_dict(mac_address_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


