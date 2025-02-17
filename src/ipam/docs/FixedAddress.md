# FixedAddress

A __FixedAddress__ object (_dhcp/fixed_address_) reserves an address for a specific client. It must have a _match_type_ and a valid corresponding _match_value_ so it can match that client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The reserved address. | [optional] 
**comment** | **str** | The description for the fixed address. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**compartment_id** | **str** | The compartment associated with the object. If no compartment is associated with the object, the value defaults to empty. | [optional] [readonly] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**dhcp_options** | [**List[OptionItem]**](OptionItem.md) | The list of DHCP options. May be either a specific option or a group of options. | [optional] 
**disable_dhcp** | **bool** | Optional. _true_ to disable object. The fixed address is converted to an exclusion when generating configuration.  Defaults to _false_. | [optional] 
**header_option_filename** | **str** | The configuration for header option filename field. | [optional] 
**header_option_server_address** | **str** | The configuration for header option server address field. | [optional] 
**header_option_server_name** | **str** | The configuration for header option server name field. | [optional] 
**hostname** | **str** | The DHCP host name associated with this fixed address. It is of FQDN type and it defaults to empty. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**inheritance_assigned_hosts** | [**List[InheritanceAssignedHost]**](InheritanceAssignedHost.md) | The list of the inheritance assigned hosts of the object. | [optional] [readonly] 
**inheritance_parent** | **str** | The resource identifier. | [optional] 
**inheritance_sources** | [**FixedAddressInheritance**](FixedAddressInheritance.md) | The inheritance configuration. | [optional] 
**ip_space** | **str** | The resource identifier. | [optional] 
**match_type** | **str** | Indicates how to match the client:  * _mac_: match the client MAC address for both IPv4 and IPv6,  * _client_text_ or _client_hex_: match the client identifier for IPv4 only,  * _relay_text_ or _relay_hex_: match the circuit ID or remote ID in the DHCP relay agent option (82) for IPv4 only,  * _duid_: match the DHCP unique identifier, currently match only for IPv6 protocol. | 
**match_value** | **str** | The value to match. | 
**name** | **str** | The name of the fixed address. May contain 1 to 256 characters. Can include UTF-8. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**tags** | **object** | The tags for the fixed address in JSON format. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 

## Example

```python
from ipam.models.fixed_address import FixedAddress

# TODO update the JSON string below
json = "{}"
# create an instance of FixedAddress from a JSON string
fixed_address_instance = FixedAddress.from_json(json)
# print the JSON string representation of the object
print(FixedAddress.to_json())

# convert the object into a dict
fixed_address_dict = fixed_address_instance.to_dict()
# create an instance of FixedAddress from a dict
fixed_address_from_dict = FixedAddress.from_dict(fixed_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


