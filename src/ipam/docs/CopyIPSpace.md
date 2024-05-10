# CopyIPSpace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The description for the copied IP space. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**copy_dhcp_options** | **bool** | Indicates whether dhcp options should be copied or not when _ipam/ip_space_ object is copied.  Defaults to _false_. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The name for the copied IP space. Must contain 1 to 256 characters. Can include UTF-8. | 
**skip_on_error** | **bool** | Indicates whether copying should skip an object in case of error and continue with next, or abort copying in case of error.  Defaults to _false_. | [optional] 

## Example

```python
from ipam.models.copy_ip_space import CopyIPSpace

# TODO update the JSON string below
json = "{}"
# create an instance of CopyIPSpace from a JSON string
copy_ip_space_instance = CopyIPSpace.from_json(json)
# print the JSON string representation of the object
print(CopyIPSpace.to_json())

# convert the object into a dict
copy_ip_space_dict = copy_ip_space_instance.to_dict()
# create an instance of CopyIPSpace from a dict
copy_ip_space_from_dict = CopyIPSpace.from_dict(copy_ip_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


