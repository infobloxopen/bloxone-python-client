# InheritedDNSSECValidationBlock

Inheritance block for fields: _dnssec_enabled_, _dnssec_enable_validation_, _dnssec_validate_expiry_, _dnssec_trust_anchors_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Defaults to _inherit_. | [optional] 
**display_name** | **str** | Human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | [**DNSSECValidationBlock**](DNSSECValidationBlock.md) | Inherited value. | [optional] [readonly] 

## Example

```python
from dns_config.models.inherited_dnssec_validation_block import InheritedDNSSECValidationBlock

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedDNSSECValidationBlock from a JSON string
inherited_dnssec_validation_block_instance = InheritedDNSSECValidationBlock.from_json(json)
# print the JSON string representation of the object
print(InheritedDNSSECValidationBlock.to_json())

# convert the object into a dict
inherited_dnssec_validation_block_dict = inherited_dnssec_validation_block_instance.to_dict()
# create an instance of InheritedDNSSECValidationBlock from a dict
inherited_dnssec_validation_block_from_dict = InheritedDNSSECValidationBlock.from_dict(inherited_dnssec_validation_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


