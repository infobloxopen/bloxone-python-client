# ReadMacAddressItemResponse

The response format to retrieve the __MacAddressItem__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**MacAddressItem**](MacAddressItem.md) | The __MacAddressItem__ object. | [optional] 

## Example

```python
from ipam.models.read_mac_address_item_response import ReadMacAddressItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadMacAddressItemResponse from a JSON string
read_mac_address_item_response_instance = ReadMacAddressItemResponse.from_json(json)
# print the JSON string representation of the object
print(ReadMacAddressItemResponse.to_json())

# convert the object into a dict
read_mac_address_item_response_dict = read_mac_address_item_response_instance.to_dict()
# create an instance of ReadMacAddressItemResponse from a dict
read_mac_address_item_response_from_dict = ReadMacAddressItemResponse.from_dict(read_mac_address_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


