# RootNS

Root nameserver

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | IPv4 address. | 
**fqdn** | **str** | FQDN. | 
**protocol_fqdn** | **str** | FQDN in punycode. | [optional] [readonly] 

## Example

```python
from dns_config.models.root_ns import RootNS

# TODO update the JSON string below
json = "{}"
# create an instance of RootNS from a JSON string
root_ns_instance = RootNS.from_json(json)
# print the JSON string representation of the object
print(RootNS.to_json())

# convert the object into a dict
root_ns_dict = root_ns_instance.to_dict()
# create an instance of RootNS from a dict
root_ns_from_dict = RootNS.from_dict(root_ns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


