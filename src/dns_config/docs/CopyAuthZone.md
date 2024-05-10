# CopyAuthZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | A comment of the (copied) _dns/auth_zone_ object. | [optional] 
**external_primaries** | [**List[ExternalPrimary]**](ExternalPrimary.md) | DNS primaries external to BloxOne DDI. Order is not significant. | [optional] 
**external_secondaries** | [**List[ExternalSecondary]**](ExternalSecondary.md) | DNS secondaries external to BloxOne DDI. Order is not significant. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**internal_secondaries** | [**List[InternalSecondary]**](InternalSecondary.md) | BloxOne DDI hosts acting as internal secondaries. Order is not significant. | [optional] 
**nsgs** | **List[str]** | The resource identifier. | [optional] 
**recursive** | **bool** | Indicates whether child objects should be copied or not.  Defaults to _false_. Reserved for future use. | [optional] 
**skip_on_error** | **bool** | Indicates whether copying should skip object in case of error and continue with next, or abort copying in case of error.  Defaults to _false_. | [optional] 
**target_view** | **str** | The resource identifier. | 

## Example

```python
from dns_config.models.copy_auth_zone import CopyAuthZone

# TODO update the JSON string below
json = "{}"
# create an instance of CopyAuthZone from a JSON string
copy_auth_zone_instance = CopyAuthZone.from_json(json)
# print the JSON string representation of the object
print(CopyAuthZone.to_json())

# convert the object into a dict
copy_auth_zone_dict = copy_auth_zone_instance.to_dict()
# create an instance of CopyAuthZone from a dict
copy_auth_zone_from_dict = CopyAuthZone.from_dict(copy_auth_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


