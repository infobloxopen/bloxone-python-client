# DNSSECValidationBlock

Block for fields: _dnssec_enabled_, _dnssec_enable_validation_, _dnssec_validate_expiry_, _dnssec_trust_anchors_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnssec_enable_validation** | **bool** | Optional. Field config for _dnssec_enable_validation_ field. | [optional] 
**dnssec_enabled** | **bool** | Optional. Field config for _dnssec_enabled_ field. | [optional] 
**dnssec_trust_anchors** | [**List[TrustAnchor]**](TrustAnchor.md) | Optional. Field config for _dnssec_trust_anchors_ field. | [optional] 
**dnssec_validate_expiry** | **bool** | Optional. Field config for _dnssec_validate_expiry_ field. | [optional] 

## Example

```python
from dns_config.models.dnssec_validation_block import DNSSECValidationBlock

# TODO update the JSON string below
json = "{}"
# create an instance of DNSSECValidationBlock from a JSON string
dnssec_validation_block_instance = DNSSECValidationBlock.from_json(json)
# print the JSON string representation of the object
print(DNSSECValidationBlock.to_json())

# convert the object into a dict
dnssec_validation_block_dict = dnssec_validation_block_instance.to_dict()
# create an instance of DNSSECValidationBlock from a dict
dnssec_validation_block_from_dict = DNSSECValidationBlock.from_dict(dnssec_validation_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


