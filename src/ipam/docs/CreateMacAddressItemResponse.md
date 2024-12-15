# CreateMacAddressItemResponse

The response format to create the __MacAddressItem__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**MacAddressItem**](MacAddressItem.md) | The created __MacAddressItem__ object. | [optional] 

## Example

```python
from ipam.models.create_mac_address_item_response import CreateMacAddressItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMacAddressItemResponse from a JSON string
create_mac_address_item_response_instance = CreateMacAddressItemResponse.from_json(json)
# print the JSON string representation of the object
print(CreateMacAddressItemResponse.to_json())

# convert the object into a dict
create_mac_address_item_response_dict = create_mac_address_item_response_instance.to_dict()
# create an instance of CreateMacAddressItemResponse from a dict
create_mac_address_item_response_from_dict = CreateMacAddressItemResponse.from_dict(create_mac_address_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


