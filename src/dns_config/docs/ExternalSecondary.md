# ExternalSecondary

External DNS secondary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | IP Address of nameserver. | 
**fqdn** | **str** | FQDN of nameserver. | 
**protocol_fqdn** | **str** | FQDN of nameserver in punycode. | [optional] [readonly] 
**stealth** | **bool** | If enabled, the NS record and glue record will NOT be automatically generated according to secondaries nameserver assignment.  Default: _false_ | [optional] 
**tsig_enabled** | **bool** | If enabled, secondaries will use the configured TSIG key when requesting a zone transfer.  Default: _false_ | [optional] 
**tsig_key** | [**TSIGKey**](TSIGKey.md) |  | [optional] 

## Example

```python
from dns_config.models.external_secondary import ExternalSecondary

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalSecondary from a JSON string
external_secondary_instance = ExternalSecondary.from_json(json)
# print the JSON string representation of the object
print(ExternalSecondary.to_json())

# convert the object into a dict
external_secondary_dict = external_secondary_instance.to_dict()
# create an instance of ExternalSecondary from a dict
external_secondary_from_dict = ExternalSecondary.from_dict(external_secondary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


