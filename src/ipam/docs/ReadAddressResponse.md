# ReadAddressResponse

The response format to retrieve the __Address__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Address**](Address.md) | The Address object. | [optional] 

## Example

```python
from ipam.models.read_address_response import ReadAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadAddressResponse from a JSON string
read_address_response_instance = ReadAddressResponse.from_json(json)
# print the JSON string representation of the object
print(ReadAddressResponse.to_json())

# convert the object into a dict
read_address_response_dict = read_address_response_instance.to_dict()
# create an instance of ReadAddressResponse from a dict
read_address_response_from_dict = ReadAddressResponse.from_dict(read_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


