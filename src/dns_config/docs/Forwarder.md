# Forwarder

External DNS server to forward to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Server IP address. | 
**fqdn** | **str** | Server FQDN. | [optional] 
**protocol_fqdn** | **str** | Server FQDN in punycode. | [optional] [readonly] 

## Example

```python
from dns_config.models.forwarder import Forwarder

# TODO update the JSON string below
json = "{}"
# create an instance of Forwarder from a JSON string
forwarder_instance = Forwarder.from_json(json)
# print the JSON string representation of the object
print(Forwarder.to_json())

# convert the object into a dict
forwarder_dict = forwarder_instance.to_dict()
# create an instance of Forwarder from a dict
forwarder_from_dict = Forwarder.from_dict(forwarder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


