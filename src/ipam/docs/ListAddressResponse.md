# ListAddressResponse

The response format to retrieve __Address__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Address]**](Address.md) | The list of Address objects. | [optional] 

## Example

```python
from ipam.models.list_address_response import ListAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAddressResponse from a JSON string
list_address_response_instance = ListAddressResponse.from_json(json)
# print the JSON string representation of the object
print(ListAddressResponse.to_json())

# convert the object into a dict
list_address_response_dict = list_address_response_instance.to_dict()
# create an instance of ListAddressResponse from a dict
list_address_response_from_dict = ListAddressResponse.from_dict(list_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


