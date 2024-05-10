# NamedListItemsInsertOrUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The Named List object identifier. | [optional] [readonly] 
**items** | **List[str]** | The list of the FQDN or IPv4/IPv6 addresses or IPv4/IPv6 CIDRs to define whitelists and blacklists for additional protection. | [optional] 
**items_described** | [**List[ItemStructs]**](ItemStructs.md) | The List of ItemStructs structure which contains the item and its description | [optional] 

## Example

```python
from fw.models.named_list_items_insert_or_update import NamedListItemsInsertOrUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NamedListItemsInsertOrUpdate from a JSON string
named_list_items_insert_or_update_instance = NamedListItemsInsertOrUpdate.from_json(json)
# print the JSON string representation of the object
print(NamedListItemsInsertOrUpdate.to_json())

# convert the object into a dict
named_list_items_insert_or_update_dict = named_list_items_insert_or_update_instance.to_dict()
# create an instance of NamedListItemsInsertOrUpdate from a dict
named_list_items_insert_or_update_from_dict = NamedListItemsInsertOrUpdate.from_dict(named_list_items_insert_or_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


