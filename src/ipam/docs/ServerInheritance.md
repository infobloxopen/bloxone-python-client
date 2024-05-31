# ServerInheritance

The inheritance configuration specifies how and which fields _Server_ object (DHCP Config Profile) inherits from _Global_ parent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ddns_block** | [**InheritedDDNSBlock**](InheritedDDNSBlock.md) | The inheritance configuration for _ddns_enabled_, _ddns_send_updates_, _ddns_domain_, _ddns_zones_ fields from _Server_ object. | [optional] 
**ddns_client_update** | [**InheritanceInheritedString**](InheritanceInheritedString.md) | The inheritance configuration for _ddns_client_update_ field from _Server_ object. | [optional] 
**ddns_conflict_resolution_mode** | [**InheritanceInheritedString**](InheritanceInheritedString.md) | The inheritance configuration for _ddns_conflict_resolution_mode_ field from _Server_ object. | [optional] 
**ddns_hostname_block** | [**InheritedDDNSHostnameBlock**](InheritedDDNSHostnameBlock.md) | The inheritance configuration for _ddns_generate_name_ and _ddns_generated_prefix_ fields from _Server_ object. | [optional] 
**ddns_ttl_percent** | [**InheritanceInheritedFloat**](InheritanceInheritedFloat.md) | The inheritance configuration for _ddns_ttl_percent_ field from _Server_ object. | [optional] 
**ddns_update_on_renew** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) | The inheritance configuration for _ddns_update_on_renew_ field from _Server_ object. | [optional] 
**ddns_use_conflict_resolution** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) | The inheritance configuration for _ddns_use_conflict_resolution_ field from _Server_ object. | [optional] 
**dhcp_config** | [**InheritedDHCPConfig**](InheritedDHCPConfig.md) | The inheritance configuration for _dhcp_config_ field from _Server_ object. | [optional] 
**dhcp_options** | [**InheritedDHCPOptionList**](InheritedDHCPOptionList.md) | The inheritance configuration for _dhcp_options_ field from _Server_ object. | [optional] 
**dhcp_options_v6** | [**InheritedDHCPOptionList**](InheritedDHCPOptionList.md) | The inheritance configuration for _dhcp_options_v6_ field from _Server_ object. | [optional] 
**header_option_filename** | [**InheritanceInheritedString**](InheritanceInheritedString.md) | The inheritance configuration for _header_option_filename_ field. | [optional] 
**header_option_server_address** | [**InheritanceInheritedString**](InheritanceInheritedString.md) | The inheritance configuration for _header_option_server_address_ field. | [optional] 
**header_option_server_name** | [**InheritanceInheritedString**](InheritanceInheritedString.md) | The inheritance configuration for _header_option_server_name_ field. | [optional] 
**hostname_rewrite_block** | [**InheritedHostnameRewriteBlock**](InheritedHostnameRewriteBlock.md) | The inheritance configuration for _hostname_rewrite_enabled_, _hostname_rewrite_regex_, _hostname_rewrite_char_ fields from _Server_ object. | [optional] 
**vendor_specific_option_option_space** | [**InheritanceInheritedIdentifier**](InheritanceInheritedIdentifier.md) | The inheritance configuration for _vendor_specific_option_option_space_ field from _Server_ object. | [optional] 

## Example

```python
from ipam.models.server_inheritance import ServerInheritance

# TODO update the JSON string below
json = "{}"
# create an instance of ServerInheritance from a JSON string
server_inheritance_instance = ServerInheritance.from_json(json)
# print the JSON string representation of the object
print(ServerInheritance.to_json())

# convert the object into a dict
server_inheritance_dict = server_inheritance_instance.to_dict()
# create an instance of ServerInheritance from a dict
server_inheritance_from_dict = ServerInheritance.from_dict(server_inheritance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


