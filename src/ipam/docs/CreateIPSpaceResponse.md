# CreateIPSpaceResponse

The response format to create the __IPSpace__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**IPSpace**](IPSpace.md) | The created IP Space object. | [optional] 

## Example

```python
from ipam.models.create_ip_space_response import CreateIPSpaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIPSpaceResponse from a JSON string
create_ip_space_response_instance = CreateIPSpaceResponse.from_json(json)
# print the JSON string representation of the object
print(CreateIPSpaceResponse.to_json())

# convert the object into a dict
create_ip_space_response_dict = create_ip_space_response_instance.to_dict()
# create an instance of CreateIPSpaceResponse from a dict
create_ip_space_response_from_dict = CreateIPSpaceResponse.from_dict(create_ip_space_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


