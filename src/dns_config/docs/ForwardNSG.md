# ForwardNSG

Forward DNS Server Group for forward zones.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for the object. | [optional] 
**external_forwarders** | [**List[Forwarder]**](Forwarder.md) | Optional. External DNS servers to forward to. Order is not significant. | [optional] 
**forwarders_only** | **bool** | Optional. _true_ to only forward. | [optional] 
**hosts** | **List[str]** | The resource identifier. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**internal_forwarders** | **List[str]** | The resource identifier. | [optional] 
**name** | **str** | Name of the object. | 
**nsgs** | **List[str]** | The resource identifier. | [optional] 
**tags** | **object** | Tagging specifics. | [optional] 

## Example

```python
from dns_config.models.forward_nsg import ForwardNSG

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardNSG from a JSON string
forward_nsg_instance = ForwardNSG.from_json(json)
# print the JSON string representation of the object
print(ForwardNSG.to_json())

# convert the object into a dict
forward_nsg_dict = forward_nsg_instance.to_dict()
# create an instance of ForwardNSG from a dict
forward_nsg_from_dict = ForwardNSG.from_dict(forward_nsg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


