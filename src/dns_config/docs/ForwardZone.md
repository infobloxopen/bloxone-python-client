# ForwardZone

Forward zone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for zone configuration. | [optional] 
**created_at** | **datetime** | The timestamp when the object has been created. | [optional] [readonly] 
**disabled** | **bool** | Optional. _true_ to disable object. A disabled object is effectively non-existent when generating configuration. | [optional] 
**external_forwarders** | [**List[Forwarder]**](Forwarder.md) | Optional. External DNS servers to forward to. Order is not significant. | [optional] 
**forward_only** | **bool** | Optional. _true_ to only forward. | [optional] 
**fqdn** | **str** | Zone FQDN. The FQDN supplied at creation will be converted to canonical form.  Read-only after creation. | [optional] 
**hosts** | **List[str]** | The resource identifier. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**internal_forwarders** | **List[str]** | The resource identifier. | [optional] 
**mapped_subnet** | **str** | Reverse zone network address in the following format: \&quot;ip-address/cidr\&quot;. Defaults to empty. | [optional] [readonly] 
**mapping** | **str** | Read-only. Zone mapping type. Allowed values:  * _forward_,  * _ipv4_reverse_.  * _ipv6_reverse_.  Defaults to _forward_. | [optional] [readonly] 
**nsgs** | **List[str]** | The resource identifier. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**protocol_fqdn** | **str** | Zone FQDN in punycode. | [optional] [readonly] 
**tags** | **object** | Tagging specifics. | [optional] 
**updated_at** | **datetime** | The timestamp when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 
**view** | **str** | The resource identifier. | [optional] 
**warnings** | [**List[Warning]**](Warning.md) | The list of a forward zone warnings. | [optional] [readonly] 

## Example

```python
from dns_config.models.forward_zone import ForwardZone

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardZone from a JSON string
forward_zone_instance = ForwardZone.from_json(json)
# print the JSON string representation of the object
print(ForwardZone.to_json())

# convert the object into a dict
forward_zone_dict = forward_zone_instance.to_dict()
# create an instance of ForwardZone from a dict
forward_zone_from_dict = ForwardZone.from_dict(forward_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


