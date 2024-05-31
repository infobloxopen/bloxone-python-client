# ExternalPrimary

External DNS primary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Optional. Required only if _type_ is _server_. IP Address of nameserver. | [optional] 
**fqdn** | **str** | Optional. Required only if _type_ is _server_. FQDN of nameserver. | [optional] 
**nsg** | **str** | The resource identifier. | [optional] 
**protocol_fqdn** | **str** | FQDN of nameserver in punycode. | [optional] [readonly] 
**tsig_enabled** | **bool** | Optional. If enabled, secondaries will use the configured TSIG key when requesting a zone transfer from this primary. | [optional] 
**tsig_key** | [**TSIGKey**](TSIGKey.md) | Optional. TSIG key.  Error if empty while _tsig_enabled_ is _true_. | [optional] 
**type** | **str** | Allowed values: * _nsg_, * _primary_. | 

## Example

```python
from dns_config.models.external_primary import ExternalPrimary

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalPrimary from a JSON string
external_primary_instance = ExternalPrimary.from_json(json)
# print the JSON string representation of the object
print(ExternalPrimary.to_json())

# convert the object into a dict
external_primary_dict = external_primary_instance.to_dict()
# create an instance of ExternalPrimary from a dict
external_primary_from_dict = ExternalPrimary.from_dict(external_primary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


