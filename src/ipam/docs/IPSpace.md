# IPSpace

An __IPSpace__ object (_ipam/ip_space_) allows customers to represent their entire managed address space with no collision. A collision arises when two or more block of addresses overlap partially or fully.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asm_config** | [**ASMConfig**](ASMConfig.md) |  | [optional] 
**asm_scope_flag** | **int** | The number of times the automated scope management usage limits have been exceeded for any of the subnets in this IP space. | [optional] [readonly] 
**comment** | **str** | The description for the IP space. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**ddns_client_update** | **str** | Controls who does the DDNS updates.  Valid values are: * _client_: DHCP server updates DNS if requested by client. * _server_: DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates. * _ignore_: DHCP server always updates DNS, even if the client says not to. * _over_client_update_: Same as _server_. DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates. * _over_no_update_: DHCP server updates DNS even if the client requests that no updates be done. If the client requests to do the update, DHCP server allows it.  Defaults to _client_. | [optional] [default to 'client']
**ddns_conflict_resolution_mode** | **str** | The mode used for resolving conflicts while performing DDNS updates.  Valid values are: * _check_with_dhcid_: It includes adding a DHCID record and checking that record via conflict detection as per RFC 4703. * _no_check_with_dhcid_: This will ignore conflict detection but add a DHCID record when creating/updating an entry. * _check_exists_with_dhcid_: This will check if there is an existing DHCID record but does not verify the value of the record matches the update. This will also update the DHCID record for the entry. * _no_check_without_dhcid_: This ignores conflict detection and will not add a DHCID record when creating/updating a DDNS entry.  Defaults to _check_with_dhcid_. | [optional] [default to 'check_with_dhcid']
**ddns_domain** | **str** | The domain suffix for DDNS updates. FQDN, may be empty.  Defaults to empty. | [optional] 
**ddns_generate_name** | **bool** | Indicates if DDNS needs to generate a hostname when not supplied by the client.  Defaults to _false_. | [optional] [default to False]
**ddns_generated_prefix** | **str** | The prefix used in the generation of an FQDN.  When generating a name, DHCP server will construct the name in the format: [ddns-generated-prefix]-[address-text].[ddns-qualifying-suffix]. where address-text is simply the lease IP address converted to a hyphenated string.  Defaults to \&quot;myhost\&quot;. | [optional] [default to 'myhost']
**ddns_send_updates** | **bool** | Determines if DDNS updates are enabled at the IP space level. Defaults to _true_. | [optional] [default to True]
**ddns_ttl_percent** | **float** | DDNS TTL value - to be calculated as a simple percentage of the lease&#39;s lifetime, using the parameter&#39;s value as the percentage. It is specified as a percentage (e.g. 25, 75). Defaults to unspecified. | [optional] 
**ddns_update_on_renew** | **bool** | Instructs the DHCP server to always update the DNS information when a lease is renewed even if its DNS information has not changed.  Defaults to _false_. | [optional] [default to False]
**ddns_use_conflict_resolution** | **bool** | When true, DHCP server will apply conflict resolution, as described in RFC 4703, when attempting to fulfill the update request.  When false, DHCP server will simply attempt to update the DNS entries per the request, regardless of whether or not they conflict with existing entries owned by other DHCP4 clients.  Defaults to _true_. | [optional] [default to True]
**dhcp_config** | [**DHCPConfig**](DHCPConfig.md) |  | [optional] 
**dhcp_options** | [**List[OptionItem]**](OptionItem.md) | The list of IPv4 DHCP options for IP space. May be either a specific option or a group of options. | [optional] 
**dhcp_options_v6** | [**List[OptionItem]**](OptionItem.md) | The list of IPv6 DHCP options for IP space. May be either a specific option or a group of options. | [optional] 
**header_option_filename** | **str** | The configuration for header option filename field. | [optional] 
**header_option_server_address** | **str** | The configuration for header option server address field. | [optional] 
**header_option_server_name** | **str** | The configuration for header option server name field. | [optional] 
**hostname_rewrite_char** | **str** | The character to replace non-matching characters with, when hostname rewrite is enabled.  Any single ASCII character or no character if the invalid characters should be removed without replacement.  Defaults to \&quot;-\&quot;. | [optional] [default to '-']
**hostname_rewrite_enabled** | **bool** | Indicates if client supplied hostnames will be rewritten prior to DDNS update by replacing every character that does not match _hostname_rewrite_regex_ by _hostname_rewrite_char_.  Defaults to _false_. | [optional] [default to False]
**hostname_rewrite_regex** | **str** | The regex bracket expression to match valid characters.  Must begin with \&quot;[\&quot; and end with \&quot;]\&quot; and be a compilable POSIX regex.  Defaults to \&quot;[^a-zA-Z0-9_.]\&quot;. | [optional] [default to '[^a-zA-Z0-9_.]']
**id** | **str** | The resource identifier. | [optional] [readonly] 
**inheritance_sources** | [**IPSpaceInheritance**](IPSpaceInheritance.md) |  | [optional] 
**name** | **str** | The name of the IP space. Must contain 1 to 256 characters. Can include UTF-8. | 
**tags** | **object** | The tags for the IP space in JSON format. | [optional] 
**threshold** | [**UtilizationThreshold**](UtilizationThreshold.md) |  | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 
**utilization** | [**Utilization**](Utilization.md) |  | [optional] 
**utilization_v6** | [**UtilizationV6**](UtilizationV6.md) |  | [optional] 
**vendor_specific_option_option_space** | **str** | The resource identifier. | [optional] 

## Example

```python
from ipam.models.ip_space import IPSpace

# TODO update the JSON string below
json = "{}"
# create an instance of IPSpace from a JSON string
ip_space_instance = IPSpace.from_json(json)
# print the JSON string representation of the object
print(IPSpace.to_json())

# convert the object into a dict
ip_space_dict = ip_space_instance.to_dict()
# create an instance of IPSpace from a dict
ip_space_from_dict = IPSpace.from_dict(ip_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


