# DHCPGlobal

The global DHCP configuration (_dhcp/global_). Used by default unless more specific configuration exists. There is only one instance of this object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asm_config** | [**ASMConfig**](ASMConfig.md) | The global Automated Scope Management configuration. | [optional] 
**client_principal** | **str** | The Kerberos principal name. It uses the typical Kerberos notation: &lt;SERVICE-NAME&gt;/&lt;server-domain-name&gt;@&lt;REALM&gt;.  Defaults to empty. | [optional] 
**ddns_client_update** | **str** | The global configuration to control who does the DDNS updates.  Valid values are: * _client_: DHCP server updates DNS if requested by client. * _server_: DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates. * _ignore_: DHCP server always updates DNS, even if the client says not to. * _over_client_update_: Same as _server_. DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates. * _over_no_update_: DHCP server updates DNS even if the client requests that no updates be done. If the client requests to do the update, DHCP server allows it.  Defaults to _client_. | [optional] 
**ddns_conflict_resolution_mode** | **str** | The mode used for resolving conflicts while performing DDNS updates.  Valid values are: * _check_with_dhcid_: It includes adding a DHCID record and checking that record via conflict detection as per RFC 4703. * _no_check_with_dhcid_: This will ignore conflict detection but add a DHCID record when creating/updating an entry. * _check_exists_with_dhcid_: This will check if there is an existing DHCID record but does not verify the value of the record matches the update. This will also update the DHCID record for the entry. * _no_check_without_dhcid_: This ignores conflict detection and will not add a DHCID record when creating/updating a DDNS entry.  Defaults to _check_with_dhcid_. | [optional] 
**ddns_domain** | **str** | The domain suffix for DDNS updates. FQDN, may be empty.  Must be specified if _ddns_enabled_ is _true_.  Defaults to empty. | [optional] 
**ddns_enabled** | **bool** | Indicates if DDNS updates should be performed for leases.  All other ddns_* configuration fields are ignored when this flag is unset.  At a minimum, _ddns_domain_ and _ddns_zones_ must be configured to enable DDNS.  Defaults to _false_. | [optional] 
**ddns_generate_name** | **bool** | Indicates if DDNS needs to generate a hostname when not supplied by the client.  Defaults to _false_. | [optional] 
**ddns_generated_prefix** | **str** | The prefix used in the generation of an FQDN.  When generating a name, DHCP server will construct the name in the format: [ddns-generated-prefix]-[address-text].[ddns-qualifying-suffix]. where address-text is simply the lease IP address converted to a hyphenated string.  Defaults to \&quot;myhost\&quot;. | [optional] 
**ddns_send_updates** | **bool** | Determines if DDNS updates are enabled at the global level. Defaults to _true_. | [optional] 
**ddns_ttl_percent** | **float** | DDNS TTL value - to be calculated as a simple percentage of the lease&#39;s lifetime, using the parameter&#39;s value as the percentage. It is specified as a percentage (e.g. 25, 75). Defaults to unspecified. | [optional] 
**ddns_update_on_renew** | **bool** | Instructs the DHCP server to always update the DNS information when a lease is renewed even if its DNS information has not changed.  Defaults to _false_. | [optional] 
**ddns_use_conflict_resolution** | **bool** | When true, DHCP server will apply conflict resolution, as described in RFC 4703, when attempting to fulfill the update request.  When false, DHCP server will simply attempt to update the DNS entries per the request, regardless of whether or not they conflict with existing entries owned by other DHCP4 clients.  Defaults to _true_. | [optional] 
**ddns_zones** | [**List[DDNSZone]**](DDNSZone.md) | DNS zones that DDNS updates can be sent to. There is no resolver fallback. The target zone must be explicitly configured for the update to be performed.  Updates are sent to the closest enclosing zone.  Error if _ddns_enabled_ is _true_ and the _ddns_domain_ does not have a corresponding entry in _ddns_zones_.  Error if there are items with duplicate zone in the list.  Defaults to empty list. | [optional] 
**dhcp_config** | [**DHCPConfig**](DHCPConfig.md) | The global DHCP configuration that controls how leases are issued. | [optional] 
**dhcp_options** | [**List[OptionItem]**](OptionItem.md) | The list of DHCP options or group of options for IPv4. An option list is ordered and may include both option groups and specific options. Multiple occurrences of the same option or group is not an error. The last occurrence of an option in the list will be used.  Error if the graph of referenced groups contains cycles.  Defaults to empty list. | [optional] 
**dhcp_options_v6** | [**List[OptionItem]**](OptionItem.md) | The list of DHCP options or group of options for IPv6. An option list is ordered and may include both option groups and specific options. Multiple occurrences of the same option or group is not an error. The last occurrence of an option in the list will be used.  Error if the graph of referenced groups contains cycles.  Defaults to empty list. | [optional] 
**dhcp_threshold** | [**DHCPUtilizationThreshold**](DHCPUtilizationThreshold.md) | The global DHCP Utilization threshold settings. | [optional] 
**gss_tsig_fallback** | **bool** | The behavior when GSS-TSIG should be used (a matching external DNS server is configured) but no GSS-TSIG key is available. If configured to _false_ (the default) this DNS server is skipped, if configured to _true_ the DNS server is ignored and the DNS update is sent with the configured DHCP-DDNS protection e.g. TSIG key or without any protection when none was configured.  Defaults to _false_. | [optional] 
**header_option_filename** | **str** | The configuration for header option filename field. | [optional] 
**header_option_server_address** | **str** | The configuration for header option server address field. | [optional] 
**header_option_server_name** | **str** | The configuration for header option server name field. | [optional] 
**hostname_rewrite_char** | **str** | The character to replace non-matching characters with, when hostname rewrite is enabled in global configuration.  Any single ASCII character or no character if the invalid characters should be removed without replacement.  Defaults to \&quot;-\&quot;. | [optional] 
**hostname_rewrite_enabled** | **bool** | The global configuration to indicate if the hostnames supplied by the client will be rewritten prior to DDNS update by replacing every character that does not match _hostname_rewrite_regex_ by _hostname_rewrite_char_.  Defaults to _false_. | [optional] 
**hostname_rewrite_regex** | **str** | The regex bracket expression to match valid characters when hostname rewrite is enabled in global configuration.  Must begin with \&quot;[\&quot; and end with \&quot;]\&quot; and be a compilable POSIX regex.  Defaults to \&quot;[^a-zA-Z0-9_.]\&quot;. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**kerberos_kdc** | **str** | Address of Kerberos Key Distribution Center.  Defaults to empty. | [optional] 
**kerberos_keys** | [**List[KerberosKey]**](KerberosKey.md) | _kerberos_keys_ contains a list of keys for GSS-TSIG signed dynamic updates.  Defaults to empty. | [optional] 
**kerberos_rekey_interval** | **int** | Time interval (in seconds) the keys for each configured external DNS server are checked for rekeying, i.e. a new key is created to replace the current usable one when its age is greater than the _kerberos_rekey_interval_ value.  Defaults to 120 seconds. | [optional] 
**kerberos_retry_interval** | **int** | Time interval (in seconds) to retry to create a key if any error occurred previously for any configured external DNS server.  Defaults to 30 seconds. | [optional] 
**kerberos_tkey_lifetime** | **int** | Lifetime (in seconds) of GSS-TSIG keys in the TKEY protocol.  Defaults to 160 seconds. | [optional] 
**kerberos_tkey_protocol** | **str** | Determines which protocol is used to establish the security context with the external DNS servers, TCP or UDP.  Defaults to _tcp_. | [optional] 
**prefer_option_12** | **bool** | When enabled, DHCP Server will prefer option 12 over option 81 in the incoming client request.  Defaults to _false_. | [optional] 
**remove_suffix_option_81** | **bool** | When enabled, DHCP Server will remove the suffix from the option 81 in the incoming client request.  Defaults to _false_. | [optional] 
**server_principal** | **str** | The Kerberos principal name of the external DNS server that will receive updates.  Defaults to empty. | [optional] 
**vendor_specific_option_option_space** | **str** | The resource identifier. | [optional] 

## Example

```python
from ipam.models.dhcp_global import DHCPGlobal

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPGlobal from a JSON string
dhcp_global_instance = DHCPGlobal.from_json(json)
# print the JSON string representation of the object
print(DHCPGlobal.to_json())

# convert the object into a dict
dhcp_global_dict = dhcp_global_instance.to_dict()
# create an instance of DHCPGlobal from a dict
dhcp_global_from_dict = DHCPGlobal.from_dict(dhcp_global_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


