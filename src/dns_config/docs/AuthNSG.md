# AuthNSG

Authoritative DNS Server Group for authoritative zones.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for the object. | [optional] 
**external_primaries** | [**List[ExternalPrimary]**](ExternalPrimary.md) | Optional. DNS primaries external to BloxOne DDI. Order is not significant. | [optional] 
**external_secondaries** | [**List[ExternalSecondary]**](ExternalSecondary.md) | DNS secondaries external to BloxOne DDI. Order is not significant. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**internal_secondaries** | [**List[InternalSecondary]**](InternalSecondary.md) | Optional. BloxOne DDI hosts acting as internal secondaries. Order is not significant. | [optional] 
**name** | **str** | Name of the object. | 
**nsgs** | **List[str]** | The resource identifier. | [optional] 
**tags** | **object** | Tagging specifics. | [optional] 

## Example

```python
from dns_config.models.auth_nsg import AuthNSG

# TODO update the JSON string below
json = "{}"
# create an instance of AuthNSG from a JSON string
auth_nsg_instance = AuthNSG.from_json(json)
# print the JSON string representation of the object
print(AuthNSG.to_json())

# convert the object into a dict
auth_nsg_dict = auth_nsg_instance.to_dict()
# create an instance of AuthNSG from a dict
auth_nsg_from_dict = AuthNSG.from_dict(auth_nsg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


