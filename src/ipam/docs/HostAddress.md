# HostAddress

The __HostAddress__ object represents addresses associated with a Host object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Field usage depends on the operation:  * For read operation, _address_ of the _Address_ corresponding to the _ref_ resource.  * For write operation, _address_ to be created if the _Address_ does not exist. Required if _ref_ is not set on write:     * If the _Address_ already exists and is already pointing to the right _Host_, the operation proceeds.     * If the _Address_ already exists and is pointing to a different _Host, the operation must abort.     * If the _Address_ already exists and is not pointing to any _Host_, it is linked to the _Host_. | [optional] 
**ref** | **str** | The resource identifier. | [optional] 
**space** | **str** | The resource identifier. | [optional] 

## Example

```python
from ipam.models.host_address import HostAddress

# TODO update the JSON string below
json = "{}"
# create an instance of HostAddress from a JSON string
host_address_instance = HostAddress.from_json(json)
# print the JSON string representation of the object
print(HostAddress.to_json())

# convert the object into a dict
host_address_dict = host_address_instance.to_dict()
# create an instance of HostAddress from a dict
host_address_from_dict = HostAddress.from_dict(host_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


