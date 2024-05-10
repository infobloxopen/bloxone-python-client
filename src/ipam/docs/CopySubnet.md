# CopySubnet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The description for the copied subnet. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**copy_dhcp_options** | **bool** | Indicates whether dhcp options should be copied or not when _ipam/subnet_ object is copied.  Defaults to _false_. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The name for the copied subnet. May contain 1 to 256 characters. Can include UTF-8. | [optional] 
**recursive** | **bool** | Indicates whether child objects should be copied or not.  Defaults to _false_. | [optional] 
**skip_on_error** | **bool** | Indicates whether copying should skip object in case of error and continue with next, or abort copying in case of error.  Defaults to _false_. | [optional] 
**space** | **str** | The resource identifier. | 

## Example

```python
from ipam.models.copy_subnet import CopySubnet

# TODO update the JSON string below
json = "{}"
# create an instance of CopySubnet from a JSON string
copy_subnet_instance = CopySubnet.from_json(json)
# print the JSON string representation of the object
print(CopySubnet.to_json())

# convert the object into a dict
copy_subnet_dict = copy_subnet_instance.to_dict()
# create an instance of CopySubnet from a dict
copy_subnet_from_dict = CopySubnet.from_dict(copy_subnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


