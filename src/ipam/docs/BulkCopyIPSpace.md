# BulkCopyIPSpace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copy_dhcp_options** | **bool** | Indicates whether dhcp options for IPv4 should be copied or not when objects (_ipam/address_block_ and _ipam/subnet_ only) are copied.  Defaults to _false_. | [optional] 
**copy_objects** | **List[str]** | The resource identifier. | 
**recursive** | **bool** | Indicates whether child objects should be copied or not.  Defaults to _false_. | [optional] 
**retain_child_compartment** | **bool** | Indicates whether the child objects are going to retain their compartment_id, or inherit from the object to copy into.  Defaults to false | [optional] 
**skip_on_error** | **bool** | Indicates whether copying should skip object in case of error and continue with next, or abort copying in case of error.  Defaults to _false_. | [optional] 
**target** | **str** | The resource identifier. | 

## Example

```python
from ipam.models.bulk_copy_ip_space import BulkCopyIPSpace

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCopyIPSpace from a JSON string
bulk_copy_ip_space_instance = BulkCopyIPSpace.from_json(json)
# print the JSON string representation of the object
print(BulkCopyIPSpace.to_json())

# convert the object into a dict
bulk_copy_ip_space_dict = bulk_copy_ip_space_instance.to_dict()
# create an instance of BulkCopyIPSpace from a dict
bulk_copy_ip_space_from_dict = BulkCopyIPSpace.from_dict(bulk_copy_ip_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


