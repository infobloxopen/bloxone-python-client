# Resolver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | address that can be used as resolver | [optional] 
**is_fallback** | **bool** | Mark it true to set default DNS resolvers that will be used in case if the BloxOne Cloud is unreachable. | [optional] 
**is_local** | **bool** | Mark it true to set internal or local DNS servers&#39; IPv4 or IPv6 addresses that are used as DNS resolvers | [optional] 
**protocols** | [**List[DNSProtocol]**](DNSProtocol.md) | The list of DNS resolver communication protocols. | [optional] 

## Example

```python
from dfp.models.resolver import Resolver

# TODO update the JSON string below
json = "{}"
# create an instance of Resolver from a JSON string
resolver_instance = Resolver.from_json(json)
# print the JSON string representation of the object
print(Resolver.to_json())

# convert the object into a dict
resolver_dict = resolver_instance.to_dict()
# create an instance of Resolver from a dict
resolver_from_dict = Resolver.from_dict(resolver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


