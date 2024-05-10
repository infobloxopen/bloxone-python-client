# DelegationServer

DNS zone delegation server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Optional. IP Address of nameserver.  Only required when fqdn of a delegation server falls under delegation fqdn | [optional] 
**fqdn** | **str** | Required. FQDN of nameserver. | 
**protocol_fqdn** | **str** | FQDN of nameserver in punycode. | [optional] [readonly] 

## Example

```python
from dns_config.models.delegation_server import DelegationServer

# TODO update the JSON string below
json = "{}"
# create an instance of DelegationServer from a JSON string
delegation_server_instance = DelegationServer.from_json(json)
# print the JSON string representation of the object
print(DelegationServer.to_json())

# convert the object into a dict
delegation_server_dict = delegation_server_instance.to_dict()
# create an instance of DelegationServer from a dict
delegation_server_from_dict = DelegationServer.from_dict(delegation_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


