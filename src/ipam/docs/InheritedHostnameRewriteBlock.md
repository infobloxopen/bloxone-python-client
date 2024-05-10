# InheritedHostnameRewriteBlock

The inheritance block for fields: _hostname_rewrite_enabled_, _hostname_rewrite_regex_, _hostname_rewrite_char_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The inheritance setting.  Valid values are: * _inherit_: Use the inherited value. * _override_: Use the value set in the object.  Defaults to _inherit_. | [optional] 
**display_name** | **str** | The human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | [**HostnameRewriteBlock**](HostnameRewriteBlock.md) |  | [optional] 

## Example

```python
from ipam.models.inherited_hostname_rewrite_block import InheritedHostnameRewriteBlock

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedHostnameRewriteBlock from a JSON string
inherited_hostname_rewrite_block_instance = InheritedHostnameRewriteBlock.from_json(json)
# print the JSON string representation of the object
print(InheritedHostnameRewriteBlock.to_json())

# convert the object into a dict
inherited_hostname_rewrite_block_dict = inherited_hostname_rewrite_block_instance.to_dict()
# create an instance of InheritedHostnameRewriteBlock from a dict
inherited_hostname_rewrite_block_from_dict = InheritedHostnameRewriteBlock.from_dict(inherited_hostname_rewrite_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


