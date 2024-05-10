# ServerInheritance

The inheritance configuration specifies how and which fields _Server_ object (DHCP Config Profile) inherits from _Global_ parent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ddns_block** | [**InheritedDDNSBlock**](InheritedDDNSBlock.md) |  | [optional] 
**ddns_client_update** | [**InheritanceInheritedString**](InheritanceInheritedString.md) |  | [optional] 
**ddns_conflict_resolution_mode** | [**InheritanceInheritedString**](InheritanceInheritedString.md) |  | [optional] 
**ddns_hostname_block** | [**InheritedDDNSHostnameBlock**](InheritedDDNSHostnameBlock.md) |  | [optional] 
**ddns_ttl_percent** | [**InheritanceInheritedFloat**](InheritanceInheritedFloat.md) |  | [optional] 
**ddns_update_on_renew** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) |  | [optional] 
**ddns_use_conflict_resolution** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) |  | [optional] 
**dhcp_config** | [**InheritedDHCPConfig**](InheritedDHCPConfig.md) |  | [optional] 
**dhcp_options** | [**InheritedDHCPOptionList**](InheritedDHCPOptionList.md) |  | [optional] 
**dhcp_options_v6** | [**InheritedDHCPOptionList**](InheritedDHCPOptionList.md) |  | [optional] 
**header_option_filename** | [**InheritanceInheritedString**](InheritanceInheritedString.md) |  | [optional] 
**header_option_server_address** | [**InheritanceInheritedString**](InheritanceInheritedString.md) |  | [optional] 
**header_option_server_name** | [**InheritanceInheritedString**](InheritanceInheritedString.md) |  | [optional] 
**hostname_rewrite_block** | [**InheritedHostnameRewriteBlock**](InheritedHostnameRewriteBlock.md) |  | [optional] 
**vendor_specific_option_option_space** | [**InheritanceInheritedIdentifier**](InheritanceInheritedIdentifier.md) |  | [optional] 

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


