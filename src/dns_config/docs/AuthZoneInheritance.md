# AuthZoneInheritance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gss_tsig_enabled** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**notify** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**query_acl** | [**InheritedACLItems**](InheritedACLItems.md) |  | [optional] 
**transfer_acl** | [**InheritedACLItems**](InheritedACLItems.md) |  | [optional] 
**update_acl** | [**InheritedACLItems**](InheritedACLItems.md) |  | [optional] 
**use_forwarders_for_subzones** | [**Inheritance2InheritedBool**](Inheritance2InheritedBool.md) |  | [optional] 
**zone_authority** | [**InheritedZoneAuthority**](InheritedZoneAuthority.md) |  | [optional] 

## Example

```python
from dns_config.models.auth_zone_inheritance import AuthZoneInheritance

# TODO update the JSON string below
json = "{}"
# create an instance of AuthZoneInheritance from a JSON string
auth_zone_inheritance_instance = AuthZoneInheritance.from_json(json)
# print the JSON string representation of the object
print(AuthZoneInheritance.to_json())

# convert the object into a dict
auth_zone_inheritance_dict = auth_zone_inheritance_instance.to_dict()
# create an instance of AuthZoneInheritance from a dict
auth_zone_inheritance_from_dict = AuthZoneInheritance.from_dict(auth_zone_inheritance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


