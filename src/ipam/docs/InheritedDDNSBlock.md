# InheritedDDNSBlock

The inheritance configuration block for dynamic DNS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The inheritance setting.  Valid values are: * _inherit_: Use the inherited value. * _override_: Use the value set in the object.  Defaults to _inherit_. | [optional] 
**display_name** | **str** | The human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | [**DDNSBlock**](DDNSBlock.md) | The inherited value. | [optional] 

## Example

```python
from ipam.models.inherited_ddns_block import InheritedDDNSBlock

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedDDNSBlock from a JSON string
inherited_ddns_block_instance = InheritedDDNSBlock.from_json(json)
# print the JSON string representation of the object
print(InheritedDDNSBlock.to_json())

# convert the object into a dict
inherited_ddns_block_dict = inherited_ddns_block_instance.to_dict()
# create an instance of InheritedDDNSBlock from a dict
inherited_ddns_block_from_dict = InheritedDDNSBlock.from_dict(inherited_ddns_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


