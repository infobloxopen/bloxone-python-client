# NamedListItemsInsertOrUpdateResponse

The Named List Items create or update response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | [**AtcfwNamedListItemsInsertOrUpdateResponseSuccess**](AtcfwNamedListItemsInsertOrUpdateResponseSuccess.md) |  | [optional] 

## Example

```python
from fw.models.named_list_items_insert_or_update_response import NamedListItemsInsertOrUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NamedListItemsInsertOrUpdateResponse from a JSON string
named_list_items_insert_or_update_response_instance = NamedListItemsInsertOrUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(NamedListItemsInsertOrUpdateResponse.to_json())

# convert the object into a dict
named_list_items_insert_or_update_response_dict = named_list_items_insert_or_update_response_instance.to_dict()
# create an instance of NamedListItemsInsertOrUpdateResponse from a dict
named_list_items_insert_or_update_response_from_dict = NamedListItemsInsertOrUpdateResponse.from_dict(named_list_items_insert_or_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


