# ZoneAuthorityMNameBlock

Block for fields: _mname_, _protocol_mname_, _use_default_mname_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mname** | **str** | Defaults to empty. | [optional] 
**protocol_mname** | **str** | Optional. Master name server in punycode.  Defaults to empty. | [optional] [readonly] 
**use_default_mname** | **bool** | Optional. Use default value for master name server.  Defaults to true. | [optional] 

## Example

```python
from dns_config.models.zone_authority_m_name_block import ZoneAuthorityMNameBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneAuthorityMNameBlock from a JSON string
zone_authority_m_name_block_instance = ZoneAuthorityMNameBlock.from_json(json)
# print the JSON string representation of the object
print(ZoneAuthorityMNameBlock.to_json())

# convert the object into a dict
zone_authority_m_name_block_dict = zone_authority_m_name_block_instance.to_dict()
# create an instance of ZoneAuthorityMNameBlock from a dict
zone_authority_m_name_block_from_dict = ZoneAuthorityMNameBlock.from_dict(zone_authority_m_name_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


