# ListMacAddressItemResponse

The response format to retrieve __MacAddressItem__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[MacAddressItem]**](MacAddressItem.md) | The list of __MacAddressItem__ objects. | [optional] 

## Example

```python
from ipam.models.list_mac_address_item_response import ListMacAddressItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListMacAddressItemResponse from a JSON string
list_mac_address_item_response_instance = ListMacAddressItemResponse.from_json(json)
# print the JSON string representation of the object
print(ListMacAddressItemResponse.to_json())

# convert the object into a dict
list_mac_address_item_response_dict = list_mac_address_item_response_instance.to_dict()
# create an instance of ListMacAddressItemResponse from a dict
list_mac_address_item_response_from_dict = ListMacAddressItemResponse.from_dict(list_mac_address_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


