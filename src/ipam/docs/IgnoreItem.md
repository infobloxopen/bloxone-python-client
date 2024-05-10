# IgnoreItem

An Ignore Item object (_dhcp/ignore_item_) represents an item in a DHCP ignore list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of ignore matching: client to ignore by client identifier (client hex or client text) or hardware to ignore by hardware identifier (MAC address). It can have one of the following values:  * _client_hex_,  * _client_text_,  * _hardware_. | 
**value** | **str** | Value to match. | 

## Example

```python
from ipam.models.ignore_item import IgnoreItem

# TODO update the JSON string below
json = "{}"
# create an instance of IgnoreItem from a JSON string
ignore_item_instance = IgnoreItem.from_json(json)
# print the JSON string representation of the object
print(IgnoreItem.to_json())

# convert the object into a dict
ignore_item_dict = ignore_item_instance.to_dict()
# create an instance of IgnoreItem from a dict
ignore_item_from_dict = IgnoreItem.from_dict(ignore_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


