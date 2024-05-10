# InheritedSortListItems

Inheritance configuration for a field of type list of _SortListItem_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Optional. Inheritance setting for a field. Defaults to _inherit_. | [optional] 
**display_name** | **str** | Human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | [**List[SortListItem]**](SortListItem.md) | Inherited value. | [optional] [readonly] 

## Example

```python
from dns_config.models.inherited_sort_list_items import InheritedSortListItems

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedSortListItems from a JSON string
inherited_sort_list_items_instance = InheritedSortListItems.from_json(json)
# print the JSON string representation of the object
print(InheritedSortListItems.to_json())

# convert the object into a dict
inherited_sort_list_items_dict = inherited_sort_list_items_instance.to_dict()
# create an instance of InheritedSortListItems from a dict
inherited_sort_list_items_from_dict = InheritedSortListItems.from_dict(inherited_sort_list_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


