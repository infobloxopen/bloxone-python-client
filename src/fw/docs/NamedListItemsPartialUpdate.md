# NamedListItemsPartialUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_items_described** | [**List[ItemStructs]**](ItemStructs.md) | The List of ItemStructs structure which contains the item and its description | [optional] 
**id** | **int** | The Named List object identifier. | [optional] [readonly] 
**inserted_items_described** | [**List[ItemStructs]**](ItemStructs.md) | The List of ItemStructs structure which contains the item and its description | [optional] 

## Example

```python
from fw.models.named_list_items_partial_update import NamedListItemsPartialUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NamedListItemsPartialUpdate from a JSON string
named_list_items_partial_update_instance = NamedListItemsPartialUpdate.from_json(json)
# print the JSON string representation of the object
print(NamedListItemsPartialUpdate.to_json())

# convert the object into a dict
named_list_items_partial_update_dict = named_list_items_partial_update_instance.to_dict()
# create an instance of NamedListItemsPartialUpdate from a dict
named_list_items_partial_update_from_dict = NamedListItemsPartialUpdate.from_dict(named_list_items_partial_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


