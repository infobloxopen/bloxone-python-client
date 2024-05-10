# ServerInheritance

Inheritance configuration specifies how and which fields _Server_ object inherits from _Global_ parent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_edns_option_in_outgoing_query** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**custom_root_ns_block** | [**InheritedCustomRootNSBlock**](InheritedCustomRootNSBlock.md) |  | [optional] 
**dnssec_validation_block** | [**InheritedDNSSECValidationBlock**](InheritedDNSSECValidationBlock.md) |  | [optional] 
**ecs_block** | [**InheritedECSBlock**](InheritedECSBlock.md) |  | [optional] 
**filter_aaaa_acl** | [**InheritedACLItems**](InheritedACLItems.md) |  | [optional] 
**filter_aaaa_on_v4** | [**Inheritance2InheritedString**](Inheritance2InheritedString.md) |  | [optional] 
**forwarders_block** | [**InheritedForwardersBlock**](InheritedForwardersBlock.md) |  | [optional] 
**gss_tsig_enabled** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**kerberos_keys** | [**InheritedKerberosKeys**](InheritedKerberosKeys.md) |  | [optional] 
**lame_ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**log_query_response** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**match_recursive_only** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**max_cache_ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**max_negative_ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**minimal_responses** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**notify** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**query_acl** | [**InheritedACLItems**](InheritedACLItems.md) |  | [optional] 
**query_port** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**recursion_acl** | [**InheritedACLItems**](InheritedACLItems.md) |  | [optional] 
**recursion_enabled** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**recursive_clients** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**resolver_query_timeout** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**secondary_axfr_query_limit** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**secondary_soa_query_limit** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**sort_list** | [**InheritedSortListItems**](InheritedSortListItems.md) |  | [optional] 
**synthesize_address_records_from_https** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**transfer_acl** | [**InheritedACLItems**](InheritedACLItems.md) |  | [optional] 
**update_acl** | [**InheritedACLItems**](InheritedACLItems.md) |  | [optional] 
**use_forwarders_for_subzones** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 

## Example

```python
from dns_config.models.server_inheritance import ServerInheritance

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


