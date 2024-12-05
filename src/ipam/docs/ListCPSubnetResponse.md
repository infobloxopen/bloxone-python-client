# ListCPSubnetResponse

The response format to retrieve subnets associated with config profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CPSubnet]**](CPSubnet.md) |  | [optional] 

## Example

```python
from ipam.models.list_cp_subnet_response import ListCPSubnetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCPSubnetResponse from a JSON string
list_cp_subnet_response_instance = ListCPSubnetResponse.from_json(json)
# print the JSON string representation of the object
print(ListCPSubnetResponse.to_json())

# convert the object into a dict
list_cp_subnet_response_dict = list_cp_subnet_response_instance.to_dict()
# create an instance of ListCPSubnetResponse from a dict
list_cp_subnet_response_from_dict = ListCPSubnetResponse.from_dict(list_cp_subnet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


