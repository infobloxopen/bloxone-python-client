# InheritedDDNSUpdateBlock

The inheritance configuration for ddns_domain and ddns_send_updates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The inheritance setting.  Valid values are: * _inherit_: Use the inherited value. * _override_: Use the value set in the object.  Defaults to _inherit_. | [optional] 
**display_name** | **str** | The human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | [**DDNSUpdateBlock**](DDNSUpdateBlock.md) | The inherited value. | [optional] [readonly] 

## Example

```python
from ipam.models.inherited_ddns_update_block import InheritedDDNSUpdateBlock

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedDDNSUpdateBlock from a JSON string
inherited_ddns_update_block_instance = InheritedDDNSUpdateBlock.from_json(json)
# print the JSON string representation of the object
print(InheritedDDNSUpdateBlock.to_json())

# convert the object into a dict
inherited_ddns_update_block_dict = inherited_ddns_update_block_instance.to_dict()
# create an instance of InheritedDDNSUpdateBlock from a dict
inherited_ddns_update_block_from_dict = InheritedDDNSUpdateBlock.from_dict(inherited_ddns_update_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


