# CreateAddressResponse

The response format to create the __Address__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Address**](Address.md) | The created Address object. | [optional] 

## Example

```python
from ipam.models.create_address_response import CreateAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAddressResponse from a JSON string
create_address_response_instance = CreateAddressResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAddressResponse.to_json())

# convert the object into a dict
create_address_response_dict = create_address_response_instance.to_dict()
# create an instance of CreateAddressResponse from a dict
create_address_response_from_dict = CreateAddressResponse.from_dict(create_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


