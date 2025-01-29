# Subnet

A __Subnet__ object (_ipam/subnet_) is a set of contiguous IP addresses in the same IP space with no gap, expressed as an address and CIDR values. It represents a set of addresses from which addresses are assigned to network equipment interfaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the subnet in the form “a.b.c.d/n” where the “/n” may be omitted. In this case, the CIDR value must be defined in the _cidr_ field. When reading, the _address_ field is always in the form “a.b.c.d”. | [optional] 
**asm_config** | [**ASMConfig**](ASMConfig.md) | The Automated Scope Management configuration for the subnet. | [optional] 
**asm_scope_flag** | **int** | Set to 1 to indicate that the subnet may run out of addresses. | [optional] [readonly] 
**cidr** | **int** | The CIDR of the subnet. This is required if _address_ does not include CIDR. | [optional] 
**comment** | **str** | The description for the subnet. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**compartment_id** | **str** | The compartment associated with the object. If no compartment is associated with the object, the value defaults to empty. | [optional] [readonly] 
**config_profiles** | **List[str]** | The resource identifier. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**ddns_client_update** | **str** | Controls who does the DDNS updates.  Valid values are: * _client_: DHCP server updates DNS if requested by client. * _server_: DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates. * _ignore_: DHCP server always updates DNS, even if the client says not to. * _over_client_update_: Same as _server_. DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates. * _over_no_update_: DHCP server updates DNS even if the client requests that no updates be done. If the client requests to do the update, DHCP server allows it.  Defaults to _client_. | [optional] 
**ddns_conflict_resolution_mode** | **str** | The mode used for resolving conflicts while performing DDNS updates.  Valid values are: * _check_with_dhcid_: It includes adding a DHCID record and checking that record via conflict detection as per RFC 4703. * _no_check_with_dhcid_: This will ignore conflict detection but add a DHCID record when creating/updating an entry. * _check_exists_with_dhcid_: This will check if there is an existing DHCID record but does not verify the value of the record matches the update. This will also update the DHCID record for the entry. * _no_check_without_dhcid_: This ignores conflict detection and will not add a DHCID record when creating/updating a DDNS entry.  Defaults to _check_with_dhcid_. | [optional] 
**ddns_domain** | **str** | The domain suffix for DDNS updates. FQDN, may be empty.  Defaults to empty. | [optional] 
**ddns_generate_name** | **bool** | Indicates if DDNS needs to generate a hostname when not supplied by the client.  Defaults to _false_. | [optional] 
**ddns_generated_prefix** | **str** | The prefix used in the generation of an FQDN.  When generating a name, DHCP server will construct the name in the format: [ddns-generated-prefix]-[address-text].[ddns-qualifying-suffix]. where address-text is simply the lease IP address converted to a hyphenated string.  Defaults to \&quot;myhost\&quot;. | [optional] 
**ddns_send_updates** | **bool** | Determines if DDNS updates are enabled at the subnet level. Defaults to _true_. | [optional] 
**ddns_ttl_percent** | **float** | DDNS TTL value - to be calculated as a simple percentage of the lease&#39;s lifetime, using the parameter&#39;s value as the percentage. It is specified as a percentage (e.g. 25, 75). Defaults to unspecified. | [optional] 
**ddns_update_on_renew** | **bool** | Instructs the DHCP server to always update the DNS information when a lease is renewed even if its DNS information has not changed.  Defaults to _false_. | [optional] 
**ddns_use_conflict_resolution** | **bool** | When true, DHCP server will apply conflict resolution, as described in RFC 4703, when attempting to fulfill the update request.  When false, DHCP server will simply attempt to update the DNS entries per the request, regardless of whether or not they conflict with existing entries owned by other DHCP4 clients.  Defaults to _true_. | [optional] 
**delegation** | **str** | The ID of the delegation associated with the subnet. | [optional] [readonly] 
**dhcp_config** | [**DHCPConfig**](DHCPConfig.md) | The DHCP configuration of the subnet that controls how leases are issued. | [optional] 
**dhcp_host** | **str** | The resource identifier. | [optional] 
**dhcp_options** | [**List[OptionItem]**](OptionItem.md) | The DHCP options of the subnet. This can either be a specific option or a group of options. | [optional] 
**dhcp_utilization** | [**DHCPUtilization**](DHCPUtilization.md) | The utilization of IP addresses within the DHCP ranges of the subnet. | [optional] [readonly] 
**disable_dhcp** | **bool** | Optional. _true_ to disable object. A disabled object is effectively non-existent when generating configuration.  Defaults to _false_. | [optional] 
**discovery_attrs** | **object** | The discovery attributes for this subnet in JSON format. | [optional] [readonly] 
**discovery_metadata** | **object** | The discovery metadata for this subnet in JSON format. | [optional] [readonly] 
**external_keys** | **object** | The external keys (source key) for this subnet in JSON format. | [optional] 
**federated_realms** | **List[str]** | Reserved for future use. | [optional] 
**header_option_filename** | **str** | The configuration for header option filename field. | [optional] 
**header_option_server_address** | **str** | The configuration for header option server address field. | [optional] 
**header_option_server_name** | **str** | The configuration for header option server name field. | [optional] 
**hostname_rewrite_char** | **str** | The character to replace non-matching characters with, when hostname rewrite is enabled.  Any single ASCII character or no character if the invalid characters should be removed without replacement.  Defaults to \&quot;-\&quot;. | [optional] 
**hostname_rewrite_enabled** | **bool** | Indicates if client supplied hostnames will be rewritten prior to DDNS update by replacing every character that does not match _hostname_rewrite_regex_ by _hostname_rewrite_char_.  Defaults to _false_. | [optional] 
**hostname_rewrite_regex** | **str** | The regex bracket expression to match valid characters.  Must begin with \&quot;[\&quot; and end with \&quot;]\&quot; and be a compilable POSIX regex.  Defaults to \&quot;[^a-zA-Z0-9_.]\&quot;. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**inheritance_assigned_hosts** | [**List[InheritanceAssignedHost]**](InheritanceAssignedHost.md) | The list of the inheritance assigned hosts of the object. | [optional] [readonly] 
**inheritance_parent** | **str** | The resource identifier. | [optional] 
**inheritance_sources** | [**DHCPInheritance**](DHCPInheritance.md) | The DHCP inheritance configuration for the subnet. | [optional] 
**name** | **str** | The name of the subnet. May contain 1 to 256 characters. Can include UTF-8. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**protocol** | **str** | The type of protocol of the subnet (_ip4_ or _ip6_). | [optional] [readonly] 
**rebind_time** | **int** | The lease rebind time (T2) in seconds. | [optional] 
**renew_time** | **int** | The lease renew time (T1) in seconds. | [optional] 
**space** | **str** | The resource identifier. | [optional] 
**tags** | **object** | The tags for the subnet in JSON format. | [optional] 
**threshold** | [**UtilizationThreshold**](UtilizationThreshold.md) | The IP address utilization threshold settings for the subnet. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 
**usage** | **List[str]** | The usage is a combination of indicators, each tracking a specific associated use. Listed below are usage indicators with their meaning:  usage indicator        | description  ---------------------- | --------------------------------  _IPAM_                 |  Subnet is managed in BloxOne DDI.  _DHCP_                 |  Subnet is served by a DHCP Host.  _DISCOVERED_           |  Subnet is discovered by some network discovery probe like Network Insight or NetMRI in NIOS. | [optional] [readonly] 
**utilization** | [**Utilization**](Utilization.md) | The IPV4 address utilization statistics of the subnet. | [optional] [readonly] 
**utilization_v6** | [**UtilizationV6**](UtilizationV6.md) | The utilization of IPV6 addresses in the subnet. | [optional] [readonly] 

## Example

```python
from ipam.models.subnet import Subnet

# TODO update the JSON string below
json = "{}"
# create an instance of Subnet from a JSON string
subnet_instance = Subnet.from_json(json)
# print the JSON string representation of the object
print(Subnet.to_json())

# convert the object into a dict
subnet_dict = subnet_instance.to_dict()
# create an instance of Subnet from a dict
subnet_from_dict = Subnet.from_dict(subnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


