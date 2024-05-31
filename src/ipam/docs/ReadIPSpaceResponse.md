# ReadIPSpaceResponse

The response format to retrieve the __IPSpace__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**IPSpace**](IPSpace.md) | The IPSpace object. | [optional] 

## Example

```python
from ipam.models.read_ip_space_response import ReadIPSpaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadIPSpaceResponse from a JSON string
read_ip_space_response_instance = ReadIPSpaceResponse.from_json(json)
# print the JSON string representation of the object
print(ReadIPSpaceResponse.to_json())

# convert the object into a dict
read_ip_space_response_dict = read_ip_space_response_instance.to_dict()
# create an instance of ReadIPSpaceResponse from a dict
read_ip_space_response_from_dict = ReadIPSpaceResponse.from_dict(read_ip_space_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


