# MultiListUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | The Named List object identifier. | [optional] 
**inserted_items_described** | [**List[ItemStructs]**](ItemStructs.md) | The List of ItemStructs structure which contains the item and its description | [optional] 

## Example

```python
from fw.models.multi_list_update import MultiListUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MultiListUpdate from a JSON string
multi_list_update_instance = MultiListUpdate.from_json(json)
# print the JSON string representation of the object
print(MultiListUpdate.to_json())

# convert the object into a dict
multi_list_update_dict = multi_list_update_instance.to_dict()
# create an instance of MultiListUpdate from a dict
multi_list_update_from_dict = MultiListUpdate.from_dict(multi_list_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


