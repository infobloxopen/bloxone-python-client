# Delegation

DNS zone delegation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for zone delegation. | [optional] 
**delegation_servers** | [**List[DelegationServer]**](DelegationServer.md) | Required. DNS zone delegation servers. Order is not significant. | [optional] 
**disabled** | **bool** | Optional. _true_ to disable object. A disabled object is effectively non-existent when generating resource records. | [optional] 
**fqdn** | **str** | Delegation FQDN. The FQDN supplied at creation will be converted to canonical form.  Read-only after creation. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**parent** | **str** | The resource identifier. | [optional] 
**protocol_fqdn** | **str** | Delegation FQDN in punycode. | [optional] [readonly] 
**tags** | **object** | Tagging specifics. | [optional] 
**view** | **str** | The resource identifier. | [optional] 

## Example

```python
from dns_config.models.delegation import Delegation

# TODO update the JSON string below
json = "{}"
# create an instance of Delegation from a JSON string
delegation_instance = Delegation.from_json(json)
# print the JSON string representation of the object
print(Delegation.to_json())

# convert the object into a dict
delegation_dict = delegation_instance.to_dict()
# create an instance of Delegation from a dict
delegation_from_dict = Delegation.from_dict(delegation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


