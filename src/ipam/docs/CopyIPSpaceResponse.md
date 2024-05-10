# CopyIPSpaceResponse

The response format to copy the __IPSpace__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CopyResponse**](CopyResponse.md) |  | [optional] 

## Example

```python
from ipam.models.copy_ip_space_response import CopyIPSpaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CopyIPSpaceResponse from a JSON string
copy_ip_space_response_instance = CopyIPSpaceResponse.from_json(json)
# print the JSON string representation of the object
print(CopyIPSpaceResponse.to_json())

# convert the object into a dict
copy_ip_space_response_dict = copy_ip_space_response_instance.to_dict()
# create an instance of CopyIPSpaceResponse from a dict
copy_ip_space_response_from_dict = CopyIPSpaceResponse.from_dict(copy_ip_space_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


