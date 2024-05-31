# ReadSubnetResponse

The response format to retrieve the __Subnet__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Subnet**](Subnet.md) | The Subnet object. | [optional] 

## Example

```python
from ipam.models.read_subnet_response import ReadSubnetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadSubnetResponse from a JSON string
read_subnet_response_instance = ReadSubnetResponse.from_json(json)
# print the JSON string representation of the object
print(ReadSubnetResponse.to_json())

# convert the object into a dict
read_subnet_response_dict = read_subnet_response_instance.to_dict()
# create an instance of ReadSubnetResponse from a dict
read_subnet_response_from_dict = ReadSubnetResponse.from_dict(read_subnet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


