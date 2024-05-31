# InheritedZoneAuthorityMNameBlock

Inheritance block for fields: _mname_, _protocol_mname_, _default_mname_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Defaults to _inherit_. | [optional] 
**display_name** | **str** | Human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | [**ZoneAuthorityMNameBlock**](ZoneAuthorityMNameBlock.md) | Inherited value. | [optional] [readonly] 

## Example

```python
from dns_config.models.inherited_zone_authority_m_name_block import InheritedZoneAuthorityMNameBlock

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedZoneAuthorityMNameBlock from a JSON string
inherited_zone_authority_m_name_block_instance = InheritedZoneAuthorityMNameBlock.from_json(json)
# print the JSON string representation of the object
print(InheritedZoneAuthorityMNameBlock.to_json())

# convert the object into a dict
inherited_zone_authority_m_name_block_dict = inherited_zone_authority_m_name_block_instance.to_dict()
# create an instance of InheritedZoneAuthorityMNameBlock from a dict
inherited_zone_authority_m_name_block_from_dict = InheritedZoneAuthorityMNameBlock.from_dict(inherited_zone_authority_m_name_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


