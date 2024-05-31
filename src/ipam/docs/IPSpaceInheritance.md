# IPSpaceInheritance

The __IPSpaceInheritance__ object specifies how and which fields _IPSpace_ object inherits from the parent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asm_config** | [**InheritedASMConfig**](InheritedASMConfig.md) | The inheritance configuration for _asm_config_ field. | [optional] 
**ddns_client_update** | [**InheritanceInheritedString**](InheritanceInheritedString.md) | The inheritance configuration for _ddns_client_update_ field from _IPSpace_ object. | [optional] 
**ddns_conflict_resolution_mode** | [**InheritanceInheritedString**](InheritanceInheritedString.md) | The inheritance configuration for _ddns_conflict_resolution_mode_ field from _IPSpace_ object. | [optional] 
**ddns_enabled** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) | The inheritance configuration for _ddns_enabled_ field. Only action allowed is &#39;inherit&#39;. | [optional] 
**ddns_hostname_block** | [**InheritedDDNSHostnameBlock**](InheritedDDNSHostnameBlock.md) | The inheritance configuration for _ddns_generate_name_ and _ddns_generated_prefix_ fields from _IPSpace_ object. | [optional] 
**ddns_ttl_percent** | [**InheritanceInheritedFloat**](InheritanceInheritedFloat.md) | The inheritance configuration for _ddns_ttl_percent_ field from _IPSpace_ object. | [optional] 
**ddns_update_block** | [**InheritedDDNSUpdateBlock**](InheritedDDNSUpdateBlock.md) | The inheritance configuration for _ddns_send_updates_ and _ddns_domain_ fields from _IPSpace_ object. | [optional] 
**ddns_update_on_renew** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) | The inheritance configuration for _ddns_update_on_renew_ field from _IPSpace_ object. | [optional] 
**ddns_use_conflict_resolution** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) | The inheritance configuration for _ddns_use_conflict_resolution_ field from _IPSpace_ object. | [optional] 
**dhcp_config** | [**InheritedDHCPConfig**](InheritedDHCPConfig.md) | The inheritance configuration for _dhcp_config_ field. | [optional] 
**dhcp_options** | [**InheritedDHCPOptionList**](InheritedDHCPOptionList.md) | The inheritance configuration for _dhcp_options_ field. | [optional] 
**dhcp_options_v6** | [**InheritedDHCPOptionList**](InheritedDHCPOptionList.md) | The inheritance configuration for _dhcp_options_v6_ field. | [optional] 
**header_option_filename** | [**InheritanceInheritedString**](InheritanceInheritedString.md) | The inheritance configuration for _header_option_filename_ field. | [optional] 
**header_option_server_address** | [**InheritanceInheritedString**](InheritanceInheritedString.md) | The inheritance configuration for _header_option_server_address_ field. | [optional] 
**header_option_server_name** | [**InheritanceInheritedString**](InheritanceInheritedString.md) | The inheritance configuration for _header_option_server_name_ field. | [optional] 
**hostname_rewrite_block** | [**InheritedHostnameRewriteBlock**](InheritedHostnameRewriteBlock.md) | The inheritance configuration for _hostname_rewrite_enabled_, _hostname_rewrite_regex_, and _hostname_rewrite_char_ fields from _IPSpace_ object. | [optional] 
**vendor_specific_option_option_space** | [**InheritanceInheritedIdentifier**](InheritanceInheritedIdentifier.md) | The inheritance configuration for _vendor_specific_option_option_space_ field. | [optional] 

## Example

```python
from ipam.models.ip_space_inheritance import IPSpaceInheritance

# TODO update the JSON string below
json = "{}"
# create an instance of IPSpaceInheritance from a JSON string
ip_space_inheritance_instance = IPSpaceInheritance.from_json(json)
# print the JSON string representation of the object
print(IPSpaceInheritance.to_json())

# convert the object into a dict
ip_space_inheritance_dict = ip_space_inheritance_instance.to_dict()
# create an instance of IPSpaceInheritance from a dict
ip_space_inheritance_from_dict = IPSpaceInheritance.from_dict(ip_space_inheritance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


