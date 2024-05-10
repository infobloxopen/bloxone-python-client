# AuthZone

Authoritative zone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for zone configuration. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**disabled** | **bool** | Optional. _true_ to disable object. A disabled object is effectively non-existent when generating configuration. | [optional] 
**external_primaries** | [**List[ExternalPrimary]**](ExternalPrimary.md) | Optional. DNS primaries external to BloxOne DDI. Order is not significant. | [optional] 
**external_providers** | [**List[AuthZoneExternalProvider]**](AuthZoneExternalProvider.md) | list of external providers for the auth zone. | [optional] [readonly] 
**external_secondaries** | [**List[ExternalSecondary]**](ExternalSecondary.md) | DNS secondaries external to BloxOne DDI. Order is not significant. | [optional] 
**fqdn** | **str** | Zone FQDN. The FQDN supplied at creation will be converted to canonical form.  Read-only after creation. | [optional] 
**gss_tsig_enabled** | **bool** | _gss_tsig_enabled_ enables/disables GSS-TSIG signed dynamic updates.  Defaults to _false_. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**inheritance_assigned_hosts** | [**List[Inheritance2AssignedHost]**](Inheritance2AssignedHost.md) | The list of the inheritance assigned hosts of the object. | [optional] [readonly] 
**inheritance_sources** | [**AuthZoneInheritance**](AuthZoneInheritance.md) |  | [optional] 
**initial_soa_serial** | **int** | On-create-only. SOA serial is allowed to be set when the authoritative zone is created. | [optional] 
**internal_secondaries** | [**List[InternalSecondary]**](InternalSecondary.md) | Optional. BloxOne DDI hosts acting as internal secondaries. Order is not significant. | [optional] 
**mapped_subnet** | **str** | Reverse zone network address in the following format: \&quot;ip-address/cidr\&quot;. Defaults to empty. | [optional] [readonly] 
**mapping** | **str** | Zone mapping type. Allowed values:  * _forward_,  * _ipv4_reverse_.  * _ipv6_reverse_.  Defaults to forward. | [optional] [readonly] 
**notify** | **bool** | Also notify all external secondary DNS servers if enabled.  Defaults to _false_. | [optional] 
**nsgs** | **List[str]** | The resource identifier. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**primary_type** | **str** | Primary type for an authoritative zone. Read only after creation. Allowed values:  * _external_: zone data owned by an external nameserver,  * _cloud_: zone data is owned by a BloxOne DDI host. | [optional] 
**protocol_fqdn** | **str** | Zone FQDN in punycode. | [optional] [readonly] 
**query_acl** | [**List[ACLItem]**](ACLItem.md) | Optional. Clients must match this ACL to make authoritative queries. Also used for recursive queries if that ACL is unset.  Defaults to empty. | [optional] 
**tags** | **object** | Tagging specifics. | [optional] 
**transfer_acl** | [**List[ACLItem]**](ACLItem.md) | Optional. Clients must match this ACL to receive zone transfers. | [optional] 
**update_acl** | [**List[ACLItem]**](ACLItem.md) | Optional. Specifies which hosts are allowed to submit Dynamic DNS updates for authoritative zones of _primary_type_ _cloud_.  Defaults to empty. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 
**use_forwarders_for_subzones** | **bool** | Optional. Use default forwarders to resolve queries for subzones.  Defaults to _true_. | [optional] 
**view** | **str** | The resource identifier. | [optional] 
**warnings** | [**List[Warning]**](Warning.md) | The list of an auth zone warnings. | [optional] [readonly] 
**zone_authority** | [**ZoneAuthority**](ZoneAuthority.md) |  | [optional] 

## Example

```python
from dns_config.models.auth_zone import AuthZone

# TODO update the JSON string below
json = "{}"
# create an instance of AuthZone from a JSON string
auth_zone_instance = AuthZone.from_json(json)
# print the JSON string representation of the object
print(AuthZone.to_json())

# convert the object into a dict
auth_zone_dict = auth_zone_instance.to_dict()
# create an instance of AuthZone from a dict
auth_zone_from_dict = AuthZone.from_dict(auth_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


