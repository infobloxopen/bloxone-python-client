# ListSubnetResponse

The response format to retrieve __Subnet__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Subnet]**](Subnet.md) | The list of Subnet objects. | [optional] 

## Example

```python
from ipam.models.list_subnet_response import ListSubnetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSubnetResponse from a JSON string
list_subnet_response_instance = ListSubnetResponse.from_json(json)
# print the JSON string representation of the object
print(ListSubnetResponse.to_json())

# convert the object into a dict
list_subnet_response_dict = list_subnet_response_instance.to_dict()
# create an instance of ListSubnetResponse from a dict
list_subnet_response_from_dict = ListSubnetResponse.from_dict(list_subnet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


