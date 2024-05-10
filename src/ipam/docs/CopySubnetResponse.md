# CopySubnetResponse

The response format to copy the __Subnet__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CopyResponse**](CopyResponse.md) |  | [optional] 

## Example

```python
from ipam.models.copy_subnet_response import CopySubnetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CopySubnetResponse from a JSON string
copy_subnet_response_instance = CopySubnetResponse.from_json(json)
# print the JSON string representation of the object
print(CopySubnetResponse.to_json())

# convert the object into a dict
copy_subnet_response_dict = copy_subnet_response_instance.to_dict()
# create an instance of CopySubnetResponse from a dict
copy_subnet_response_from_dict = CopySubnetResponse.from_dict(copy_subnet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


