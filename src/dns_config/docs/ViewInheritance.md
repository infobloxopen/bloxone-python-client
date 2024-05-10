# ViewInheritance

Inheritance configuration specifies how and which fields _View_ object inherits from [ _Global_, _Server_ ] parent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_edns_option_in_outgoing_query** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**custom_root_ns_block** | [**InheritedCustomRootNSBlock**](InheritedCustomRootNSBlock.md) |  | [optional] 
**dnssec_validation_block** | [**InheritedDNSSECValidationBlock**](InheritedDNSSECValidationBlock.md) |  | [optional] 
**dtc_config** | [**InheritedDtcConfig**](InheritedDtcConfig.md) |  | [optional] 
**ecs_block** | [**InheritedECSBlock**](InheritedECSBlock.md) |  | [optional] 
**edns_udp_size** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**filter_aaaa_acl** | [**InheritedACLItems**](InheritedACLItems.md) |  | [optional] 
**filter_aaaa_on_v4** | [**Inheritance2InheritedString**](Inheritance2InheritedString.md) |  | [optional] 
**forwarders_block** | [**InheritedForwardersBlock**](InheritedForwardersBlock.md) |  | [optional] 
**gss_tsig_enabled** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**lame_ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**match_recursive_only** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**max_cache_ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**max_negative_ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**max_udp_size** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**minimal_responses** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**notify** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**query_acl** | [**InheritedACLItems**](InheritedACLItems.md) |  | [optional] 
**recursion_acl** | [**InheritedACLItems**](InheritedACLItems.md) |  | [optional] 
**recursion_enabled** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**sort_list** | [**InheritedSortListItems**](InheritedSortListItems.md) |  | [optional] 
**synthesize_address_records_from_https** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**transfer_acl** | [**InheritedACLItems**](InheritedACLItems.md) |  | [optional] 
**update_acl** | [**InheritedACLItems**](InheritedACLItems.md) |  | [optional] 
**use_forwarders_for_subzones** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**zone_authority** | [**InheritedZoneAuthority**](InheritedZoneAuthority.md) |  | [optional] 

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


