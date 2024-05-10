# InheritedZoneAuthority

Inheritance configuration for a field of type _ZoneAuthority_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**expire** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**mname_block** | [**InheritedZoneAuthorityMNameBlock**](InheritedZoneAuthorityMNameBlock.md) |  | [optional] 
**negative_ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**protocol_rname** | [**Inheritance2InheritedString**](Inheritance2InheritedString.md) |  | [optional] 
**refresh** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**retry** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 
**rname** | [**Inheritance2InheritedString**](Inheritance2InheritedString.md) |  | [optional] 

## Example

```python
from dns_config.models.inherited_zone_authority import InheritedZoneAuthority

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedZoneAuthority from a JSON string
inherited_zone_authority_instance = InheritedZoneAuthority.from_json(json)
# print the JSON string representation of the object
print(InheritedZoneAuthority.to_json())

# convert the object into a dict
inherited_zone_authority_dict = inherited_zone_authority_instance.to_dict()
# create an instance of InheritedZoneAuthority from a dict
inherited_zone_authority_from_dict = InheritedZoneAuthority.from_dict(inherited_zone_authority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


