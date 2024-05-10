# InheritedACLItems

Inheritance configuration for a field of type list of _ACLItem_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Optional. Inheritance setting for a field. Defaults to _inherit_. | [optional] 
**display_name** | **str** | Human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | [**List[ACLItem]**](ACLItem.md) | Inherited value. | [optional] [readonly] 

## Example

```python
from dns_config.models.inherited_acl_items import InheritedACLItems

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedACLItems from a JSON string
inherited_acl_items_instance = InheritedACLItems.from_json(json)
# print the JSON string representation of the object
print(InheritedACLItems.to_json())

# convert the object into a dict
inherited_acl_items_dict = inherited_acl_items_instance.to_dict()
# create an instance of InheritedACLItems from a dict
inherited_acl_items_from_dict = InheritedACLItems.from_dict(inherited_acl_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


