# ZoneAuthority

Construct for fields: _refresh_, _retry_, _expire_, _default_ttl_, _negative_ttl_, _rname_, _protocol_rname_, _mname_, _protocol_mname_, _use_default_mname_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_ttl** | **int** | Optional. ZoneAuthority default ttl for resource records in zone (value in seconds).  Defaults to 28800. | [optional] 
**expire** | **int** | Optional. ZoneAuthority expire time in seconds.  Defaults to 2419200. | [optional] 
**mname** | **str** | Defaults to empty. | [optional] 
**negative_ttl** | **int** | Optional. ZoneAuthority negative caching (minimum) ttl in seconds.  Defaults to 900. | [optional] 
**protocol_mname** | **str** | Optional. ZoneAuthority master name server in punycode.  Defaults to empty. | [optional] [readonly] 
**protocol_rname** | **str** | Optional. A domain name which specifies the mailbox of the person responsible for this zone.  Defaults to empty. | [optional] [readonly] 
**refresh** | **int** | Optional. ZoneAuthority refresh.  Defaults to 10800. | [optional] 
**retry** | **int** | Optional. ZoneAuthority retry.  Defaults to 3600. | [optional] 
**rname** | **str** | Optional. ZoneAuthority rname.  Defaults to empty. | [optional] 
**use_default_mname** | **bool** | Optional. Use default value for master name server.  Defaults to true. | [optional] 

## Example

```python
from dns_config.models.zone_authority import ZoneAuthority

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneAuthority from a JSON string
zone_authority_instance = ZoneAuthority.from_json(json)
# print the JSON string representation of the object
print(ZoneAuthority.to_json())

# convert the object into a dict
zone_authority_dict = zone_authority_instance.to_dict()
# create an instance of ZoneAuthority from a dict
zone_authority_from_dict = ZoneAuthority.from_dict(zone_authority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


