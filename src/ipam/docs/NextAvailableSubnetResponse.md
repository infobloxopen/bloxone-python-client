# NextAvailableSubnetResponse

The Next Available Subnet object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Subnet]**](Subnet.md) | The list of Next Available Subnet objects. | [optional] 

## Example

```python
from ipam.models.next_available_subnet_response import NextAvailableSubnetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NextAvailableSubnetResponse from a JSON string
next_available_subnet_response_instance = NextAvailableSubnetResponse.from_json(json)
# print the JSON string representation of the object
print(NextAvailableSubnetResponse.to_json())

# convert the object into a dict
next_available_subnet_response_dict = next_available_subnet_response_instance.to_dict()
# create an instance of NextAvailableSubnetResponse from a dict
next_available_subnet_response_from_dict = NextAvailableSubnetResponse.from_dict(next_available_subnet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


