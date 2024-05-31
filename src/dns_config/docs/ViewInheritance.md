# ViewInheritance

Inheritance configuration specifies how and which fields _View_ object inherits from [ _Global_, _Server_ ] parent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_edns_option_in_outgoing_query** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) | Field config for _add_edns_option_in_outgoing_query_ field from _View_ object. | [optional] 
**custom_root_ns_block** | [**InheritedCustomRootNSBlock**](InheritedCustomRootNSBlock.md) | Optional. Field config for _custom_root_ns_block_ field from _View_ object. | [optional] 
**dnssec_validation_block** | [**InheritedDNSSECValidationBlock**](InheritedDNSSECValidationBlock.md) | Optional. Field config for _dnssec_validation_block_ field from _View_ object. | [optional] 
**dtc_config** | [**InheritedDtcConfig**](InheritedDtcConfig.md) | Optional. Field config for _dtc_config_ field from _View_ object. | [optional] 
**ecs_block** | [**InheritedECSBlock**](InheritedECSBlock.md) | Optional. Field config for _ecs_block_ field from _View_ object. | [optional] 
**edns_udp_size** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) | Optional. Field config for _edns_udp_size_ field from [View] object. | [optional] 
**filter_aaaa_acl** | [**InheritedACLItems**](InheritedACLItems.md) | Optional. Field config for _filter_aaaa_acl_ field from _View_ object. | [optional] 
**filter_aaaa_on_v4** | [**Inheritance2InheritedString**](Inheritance2InheritedString.md) | Optional. Field config for _filter_aaaa_on_v4_ field from _View_ object. | [optional] 
**forwarders_block** | [**InheritedForwardersBlock**](InheritedForwardersBlock.md) | Optional. Field config for _forwarders_block_ field from _View_ object. | [optional] 
**gss_tsig_enabled** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) | Optional. Field config for _gss_tsig_enabled_ field from _View_ object. | [optional] 
**lame_ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) | Optional. Field config for _lame_ttl_ field from _View_ object. | [optional] 
**match_recursive_only** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) | Optional. Field config for _match_recursive_only_ field from _View_ object. | [optional] 
**max_cache_ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) | Optional. Field config for _max_cache_ttl_ field from _View_ object. | [optional] 
**max_negative_ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) | Optional. Field config for _max_negative_ttl_ field from _View_ object. | [optional] 
**max_udp_size** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) | Optional. Field config for _max_udp_size_ field from [View] object. | [optional] 
**minimal_responses** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) | Optional. Field config for _minimal_responses_ field from _View_ object. | [optional] 
**notify** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) | Field config for _notify_ field from _View_ object. | [optional] 
**query_acl** | [**InheritedACLItems**](InheritedACLItems.md) | Optional. Field config for _query_acl_ field from _View_ object. | [optional] 
**recursion_acl** | [**InheritedACLItems**](InheritedACLItems.md) | Optional. Field config for _recursion_acl_ field from _View_ object. | [optional] 
**recursion_enabled** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) | Optional. Field config for _recursion_enabled_ field from _View_ object. | [optional] 
**sort_list** | [**InheritedSortListItems**](InheritedSortListItems.md) | Optional. Field config for _sort_list_ field from _View_ object. | [optional] 
**synthesize_address_records_from_https** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) | Field config for _synthesize_address_records_from_https_ field from _View_ object. | [optional] 
**transfer_acl** | [**InheritedACLItems**](InheritedACLItems.md) | Optional. Field config for _transfer_acl_ field from _View_ object. | [optional] 
**update_acl** | [**InheritedACLItems**](InheritedACLItems.md) | Optional. Field config for _update_acl_ field from _View_ object. | [optional] 
**use_forwarders_for_subzones** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) | Optional. Field config for _use_forwarders_for_subzones_ field from _View_ object. | [optional] 
**zone_authority** | [**InheritedZoneAuthority**](InheritedZoneAuthority.md) | Optional. Field config for _zone_authority_ field from _View_ object. | [optional] 

## Example

```python
from dns_config.models.view_inheritance import ViewInheritance

# TODO update the JSON string below
json = "{}"
# create an instance of ViewInheritance from a JSON string
view_inheritance_instance = ViewInheritance.from_json(json)
# print the JSON string representation of the object
print(ViewInheritance.to_json())

# convert the object into a dict
view_inheritance_dict = view_inheritance_instance.to_dict()
# create an instance of ViewInheritance from a dict
view_inheritance_from_dict = ViewInheritance.from_dict(view_inheritance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


