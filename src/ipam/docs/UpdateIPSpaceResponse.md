# UpdateIPSpaceResponse

The response format to update the __IPSpace__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**IPSpace**](IPSpace.md) | The IPSpace object. | [optional] 

## Example

```python
from ipam.models.update_ip_space_response import UpdateIPSpaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIPSpaceResponse from a JSON string
update_ip_space_response_instance = UpdateIPSpaceResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateIPSpaceResponse.to_json())

# convert the object into a dict
update_ip_space_response_dict = update_ip_space_response_instance.to_dict()
# create an instance of UpdateIPSpaceResponse from a dict
update_ip_space_response_from_dict = UpdateIPSpaceResponse.from_dict(update_ip_space_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


