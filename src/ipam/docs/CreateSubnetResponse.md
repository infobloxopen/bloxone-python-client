# CreateSubnetResponse

The response format to create the __Subnet__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Subnet**](Subnet.md) |  | [optional] 

## Example

```python
from ipam.models.create_subnet_response import CreateSubnetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubnetResponse from a JSON string
create_subnet_response_instance = CreateSubnetResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSubnetResponse.to_json())

# convert the object into a dict
create_subnet_response_dict = create_subnet_response_instance.to_dict()
# create an instance of CreateSubnetResponse from a dict
create_subnet_response_from_dict = CreateSubnetResponse.from_dict(create_subnet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


