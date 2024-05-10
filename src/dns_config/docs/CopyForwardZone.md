# CopyForwardZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | A comment of the (copied) _dns/forward_zone_ object. | [optional] 
**external_forwarders** | [**List[Forwarder]**](Forwarder.md) | Optional. External DNS servers to forward to. Order is not significant. | [optional] 
**hosts** | **List[str]** | The resource identifier. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**internal_forwarders** | **List[str]** | The resource identifier. | [optional] 
**nsgs** | **List[str]** | The resource identifier. | [optional] 
**recursive** | **bool** | Indicates whether child objects should be copied or not.  Defaults to _false_. Reserved for future use. | [optional] 
**skip_on_error** | **bool** | Indicates whether copying should skip object in case of error and continue with next, or abort copying in case of error.  Defaults to _false_. | [optional] 
**target_view** | **str** | The resource identifier. | 

## Example

```python
from dns_config.models.copy_forward_zone import CopyForwardZone

# TODO update the JSON string below
json = "{}"
# create an instance of CopyForwardZone from a JSON string
copy_forward_zone_instance = CopyForwardZone.from_json(json)
# print the JSON string representation of the object
print(CopyForwardZone.to_json())

# convert the object into a dict
copy_forward_zone_dict = copy_forward_zone_instance.to_dict()
# create an instance of CopyForwardZone from a dict
copy_forward_zone_from_dict = CopyForwardZone.from_dict(copy_forward_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


