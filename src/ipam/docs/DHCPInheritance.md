# DHCPInheritance

The __DHCPInheritance__ object specifies how the _dhcp_config_, _dhcp_options_ and _asm_config_ configuration fields are inherited from the parent object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asm_config** | [**InheritedASMConfig**](InheritedASMConfig.md) |  | [optional] 
**ddns_client_update** | [**InheritanceInheritedString**](InheritanceInheritedString.md) |  | [optional] 
**ddns_conflict_resolution_mode** | [**InheritanceInheritedString**](InheritanceInheritedString.md) |  | [optional] 
**ddns_enabled** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) |  | [optional] 
**ddns_hostname_block** | [**InheritedDDNSHostnameBlock**](InheritedDDNSHostnameBlock.md) |  | [optional] 
**ddns_ttl_percent** | [**InheritanceInheritedFloat**](InheritanceInheritedFloat.md) |  | [optional] 
**ddns_update_block** | [**InheritedDDNSUpdateBlock**](InheritedDDNSUpdateBlock.md) |  | [optional] 
**ddns_update_on_renew** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) |  | [optional] 
**ddns_use_conflict_resolution** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) |  | [optional] 
**dhcp_config** | [**InheritedDHCPConfig**](InheritedDHCPConfig.md) |  | [optional] 
**dhcp_options** | [**InheritedDHCPOptionList**](InheritedDHCPOptionList.md) |  | [optional] 
**header_option_filename** | [**InheritanceInheritedString**](InheritanceInheritedString.md) |  | [optional] 
**header_option_server_address** | [**InheritanceInheritedString**](InheritanceInheritedString.md) |  | [optional] 
**header_option_server_name** | [**InheritanceInheritedString**](InheritanceInheritedString.md) |  | [optional] 
**hostname_rewrite_block** | [**InheritedHostnameRewriteBlock**](InheritedHostnameRewriteBlock.md) |  | [optional] 

## Example

```python
from ipam.models.dhcp_inheritance import DHCPInheritance

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPInheritance from a JSON string
dhcp_inheritance_instance = DHCPInheritance.from_json(json)
# print the JSON string representation of the object
print(DHCPInheritance.to_json())

# convert the object into a dict
dhcp_inheritance_dict = dhcp_inheritance_instance.to_dict()
# create an instance of DHCPInheritance from a dict
dhcp_inheritance_from_dict = DHCPInheritance.from_dict(dhcp_inheritance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


