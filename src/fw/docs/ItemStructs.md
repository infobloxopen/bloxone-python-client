# ItemStructs

The Items Structure which contains the item and its description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the item | [optional] 
**item** | **str** | The data of the Item | [optional] 

## Example

```python
from fw.models.item_structs import ItemStructs

# TODO update the JSON string below
json = "{}"
# create an instance of ItemStructs from a JSON string
item_structs_instance = ItemStructs.from_json(json)
# print the JSON string representation of the object
print(ItemStructs.to_json())

# convert the object into a dict
item_structs_dict = item_structs_instance.to_dict()
# create an instance of ItemStructs from a dict
item_structs_from_dict = ItemStructs.from_dict(item_structs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


