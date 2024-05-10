# SortListItem

Element in a SortList.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | **str** | The resource identifier. | [optional] 
**element** | **str** | Type of element.  Allowed values:  * _any_,  * _ip_,  * _acl_, | 
**prioritized_networks** | **List[str]** | Optional. The prioritized networks. If empty, the value of _source_ or networks from _acl_ is used. | [optional] 
**source** | **str** | Must be empty if _element_ is not _ip_. | [optional] 

## Example

```python
from dns_config.models.sort_list_item import SortListItem

# TODO update the JSON string below
json = "{}"
# create an instance of SortListItem from a JSON string
sort_list_item_instance = SortListItem.from_json(json)
# print the JSON string representation of the object
print(SortListItem.to_json())

# convert the object into a dict
sort_list_item_dict = sort_list_item_instance.to_dict()
# create an instance of SortListItem from a dict
sort_list_item_from_dict = SortListItem.from_dict(sort_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


