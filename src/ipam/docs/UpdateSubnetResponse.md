# UpdateSubnetResponse

The response format to update the __Subnet__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Subnet**](Subnet.md) | The Subnet object. | [optional] 

## Example

```python
from ipam.models.update_subnet_response import UpdateSubnetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubnetResponse from a JSON string
update_subnet_response_instance = UpdateSubnetResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateSubnetResponse.to_json())

# convert the object into a dict
update_subnet_response_dict = update_subnet_response_instance.to_dict()
# create an instance of UpdateSubnetResponse from a dict
update_subnet_response_from_dict = UpdateSubnetResponse.from_dict(update_subnet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


