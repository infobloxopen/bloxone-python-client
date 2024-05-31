# View

Named collection of DNS View settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_edns_option_in_outgoing_query** | **bool** | _add_edns_option_in_outgoing_query_ adds client IP, MAC address and view name into outgoing recursive query. Defaults to _false_. | [optional] 
**comment** | **str** | Optional. Comment for view. | [optional] 
**created_at** | **datetime** | The timestamp when the object has been created. | [optional] [readonly] 
**custom_root_ns** | [**List[RootNS]**](RootNS.md) | Optional. List of custom root nameservers. The order does not matter.  Error if empty while _custom_root_ns_enabled_ is _true_. Error if there are duplicate items in the list.  Defaults to empty. | [optional] 
**custom_root_ns_enabled** | **bool** | Optional. _true_ to use custom root nameservers instead of the default ones.  The _custom_root_ns_ is validated when enabled.  Defaults to _false_. | [optional] 
**disabled** | **bool** | Optional. _true_ to disable object. A disabled object is effectively non-existent when generating configuration. | [optional] 
**dnssec_enable_validation** | **bool** | Optional. _true_ to perform DNSSEC validation. Ignored if _dnssec_enabled_ is _false_.  Defaults to _true_. | [optional] 
**dnssec_enabled** | **bool** | Optional. Master toggle for all DNSSEC processing. Other _dnssec_*_ configuration is unused if this is disabled.  Defaults to _true_. | [optional] 
**dnssec_root_keys** | [**List[TrustAnchor]**](TrustAnchor.md) | DNSSEC root keys. The root keys are not configurable.  A default list is provided by cloud management and included here for config generation. | [optional] [readonly] 
**dnssec_trust_anchors** | [**List[TrustAnchor]**](TrustAnchor.md) | Optional. DNSSEC trust anchors.  Error if there are list items with duplicate (_zone_, _sep_, _algorithm_) combinations.  Defaults to empty. | [optional] 
**dnssec_validate_expiry** | **bool** | Optional. _true_ to reject expired DNSSEC keys. Ignored if either _dnssec_enabled_ or _dnssec_enable_validation_ is _false_.  Defaults to _true_. | [optional] 
**dtc_config** | [**DTCConfig**](DTCConfig.md) | Optional. DTC configuration. | [optional] 
**ecs_enabled** | **bool** | Optional. _true_ to enable EDNS client subnet for recursive queries. Other _ecs_*_ fields are ignored if this field is not enabled.  Defaults to _false-. | [optional] 
**ecs_forwarding** | **bool** | Optional. _true_ to enable ECS options in outbound queries. This functionality has additional overhead so it is disabled by default.  Defaults to _false_. | [optional] 
**ecs_prefix_v4** | **int** | Optional. Maximum scope length for v4 ECS.  Unsigned integer, min 1 max 24  Defaults to 24. | [optional] 
**ecs_prefix_v6** | **int** | Optional. Maximum scope length for v6 ECS.  Unsigned integer, min 1 max 56  Defaults to 56. | [optional] 
**ecs_zones** | [**List[ECSZone]**](ECSZone.md) | Optional. List of zones where ECS queries may be sent.  Error if empty while _ecs_enabled_ is _true_. Error if there are duplicate FQDNs in the list.  Defaults to empty. | [optional] 
**edns_udp_size** | **int** | Optional. _edns_udp_size_ represents the edns UDP size. The size a querying DNS server advertises to the DNS server it’s sending a query to.  Defaults to 1232 bytes. | [optional] 
**filter_aaaa_acl** | [**List[ACLItem]**](ACLItem.md) | Optional. Specifies a list of client addresses for which AAAA filtering is to be applied.  Defaults to _empty_. | [optional] 
**filter_aaaa_on_v4** | **str** | _filter_aaaa_on_v4_ allows named to omit some IPv6 addresses when responding to IPv4 clients.  Allowed values: * _yes_, * _no_, * _break_dnssec_.  Defaults to _no_ | [optional] 
**forwarders** | [**List[Forwarder]**](Forwarder.md) | Optional. List of forwarders.  Error if empty while _forwarders_only_ or _use_root_forwarders_for_local_resolution_with_b1td_ is _true_. Error if there are items in the list with duplicate addresses.  Defaults to empty. | [optional] 
**forwarders_only** | **bool** | Optional. _true_ to only forward.  Defaults to _false_. | [optional] 
**gss_tsig_enabled** | **bool** | _gss_tsig_enabled_ enables/disables GSS-TSIG signed dynamic updates.  Defaults to _false_. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**inheritance_sources** | [**ViewInheritance**](ViewInheritance.md) | Optional. Inheritance configuration. | [optional] 
**ip_spaces** | **List[str]** | The resource identifier. | [optional] 
**lame_ttl** | **int** | Optional. Unused in the current on-prem DNS server implementation.  Unsigned integer, min 0 max 3600 (1h).  Defaults to 600. | [optional] 
**match_clients_acl** | [**List[ACLItem]**](ACLItem.md) | Optional. Specifies which clients have access to the view.  Defaults to empty. | [optional] 
**match_destinations_acl** | [**List[ACLItem]**](ACLItem.md) | Optional. Specifies which destination addresses have access to the view.  Defaults to empty. | [optional] 
**match_recursive_only** | **bool** | Optional. If _true_ only recursive queries from matching clients access the view.  Defaults to _false_. | [optional] 
**max_cache_ttl** | **int** | Optional. Seconds to cache positive responses.  Unsigned integer, min 1 max 604800 (7d).  Defaults to 604800 (7d). | [optional] 
**max_negative_ttl** | **int** | Optional. Seconds to cache negative responses.  Unsigned integer, min 1 max 604800 (7d).  Defaults to 10800 (3h). | [optional] 
**max_udp_size** | **int** | Optional. _max_udp_size_ represents maximum UDP payload size. The maximum number of bytes a responding DNS server will send to a UDP datagram.  Defaults to 1232 bytes. | [optional] 
**minimal_responses** | **bool** | Optional. When enabled, the DNS server will only add records to the authority and additional data sections when they are required.  Defaults to _false_. | [optional] 
**name** | **str** | Name of view. | 
**notify** | **bool** | _notify_ all external secondary DNS servers.  Defaults to _false_. | [optional] 
**query_acl** | [**List[ACLItem]**](ACLItem.md) | Optional. Clients must match this ACL to make authoritative queries. Also used for recursive queries if that ACL is unset.  Defaults to empty. | [optional] 
**recursion_acl** | [**List[ACLItem]**](ACLItem.md) | Optional. Clients must match this ACL to make recursive queries. If this ACL is empty, then the _query_acl_ will be used instead.  Defaults to empty. | [optional] 
**recursion_enabled** | **bool** | Optional. _true_ to allow recursive DNS queries.  Defaults to _true_. | [optional] 
**sort_list** | [**List[SortListItem]**](SortListItem.md) | Optional. Specifies a sorted network list for A/AAAA records in DNS query response.  Defaults to _empty_. | [optional] 
**synthesize_address_records_from_https** | **bool** | _synthesize_address_records_from_https_ enables/disables creation of A/AAAA records from HTTPS RR Defaults to _false_. | [optional] 
**tags** | **object** | Tagging specifics. | [optional] 
**transfer_acl** | [**List[ACLItem]**](ACLItem.md) | Optional. Clients must match this ACL to receive zone transfers.  Defaults to empty. | [optional] 
**update_acl** | [**List[ACLItem]**](ACLItem.md) | Optional. Specifies which hosts are allowed to issue Dynamic DNS updates for authoritative zones of _primary_type_ _cloud_.  Defaults to empty. | [optional] 
**updated_at** | **datetime** | The timestamp when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 
**use_forwarders_for_subzones** | **bool** | Optional. Use default forwarders to resolve queries for subzones.  Defaults to _true_. | [optional] 
**use_root_forwarders_for_local_resolution_with_b1td** | **bool** | _use_root_forwarders_for_local_resolution_with_b1td_ allows DNS recursive queries sent to root forwarders for local resolution when deployed alongside BloxOne Thread Defense. Defaults to _false_. | [optional] 
**zone_authority** | [**ZoneAuthority**](ZoneAuthority.md) | Optional. ZoneAuthority. | [optional] 

## Example

```python
from dns_config.models.view import View

# TODO update the JSON string below
json = "{}"
# create an instance of View from a JSON string
view_instance = View.from_json(json)
# print the JSON string representation of the object
print(View.to_json())

# convert the object into a dict
view_dict = view_instance.to_dict()
# create an instance of View from a dict
view_from_dict = View.from_dict(view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


