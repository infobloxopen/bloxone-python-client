# CreateNextAvailableSubnetResponse

The Next Available Subnet object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Subnet]**](Subnet.md) | The list of Next Available Subnet objects. | [optional] 

## Example

```python
from ipam.models.create_next_available_subnet_response import CreateNextAvailableSubnetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNextAvailableSubnetResponse from a JSON string
create_next_available_subnet_response_instance = CreateNextAvailableSubnetResponse.from_json(json)
# print the JSON string representation of the object
print(CreateNextAvailableSubnetResponse.to_json())

# convert the object into a dict
create_next_available_subnet_response_dict = create_next_available_subnet_response_instance.to_dict()
# create an instance of CreateNextAvailableSubnetResponse from a dict
create_next_available_subnet_response_from_dict = CreateNextAvailableSubnetResponse.from_dict(create_next_available_subnet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


