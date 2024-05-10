# InternalDomainsItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_items_described** | [**List[ItemStructs]**](ItemStructs.md) | The List of ItemStructs structure which contains the item and its description | [optional] 
**id** | **int** | The Internal Domain List object identifier. | [optional] [readonly] 
**inserted_items_described** | [**List[ItemStructs]**](ItemStructs.md) | The List of ItemStructs structure which contains the item and its description | [optional] 

## Example

```python
from fw.models.internal_domains_items import InternalDomainsItems

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDomainsItems from a JSON string
internal_domains_items_instance = InternalDomainsItems.from_json(json)
# print the JSON string representation of the object
print(InternalDomainsItems.to_json())

# convert the object into a dict
internal_domains_items_dict = internal_domains_items_instance.to_dict()
# create an instance of InternalDomainsItems from a dict
internal_domains_items_from_dict = InternalDomainsItems.from_dict(internal_domains_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


