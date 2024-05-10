# LBDN

A LBDN (_dtc/lbdn_) represents a load-balanced domain name

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for __LBDN__. | [optional] 
**disabled** | **bool** | Optional. _true_ to disable object. A disabled object is effectively non-existent when generating configuration. | [optional] 
**dtc_policy** | [**DTCPolicy**](DTCPolicy.md) |  | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**inheritance_sources** | [**TTLInheritance**](TTLInheritance.md) |  | [optional] 
**name** | **str** | Name of __LBDN__. | 
**precedence** | **int** | Optional. Precedence. | [optional] 
**tags** | **object** | Optional. The tags for __LBDN__ in JSON format. | [optional] 
**ttl** | **int** | Optional. Time to live value (in seconds) to be used for records in DTC response. Unsigned integer, min: 0, max 2147483647 (31-bits per RFC-2181). | [optional] 
**view** | **str** | The resource identifier. | 

## Example

```python
from dns_config.models.lbdn import LBDN

# TODO update the JSON string below
json = "{}"
# create an instance of LBDN from a JSON string
lbdn_instance = LBDN.from_json(json)
# print the JSON string representation of the object
print(LBDN.to_json())

# convert the object into a dict
lbdn_dict = lbdn_instance.to_dict()
# create an instance of LBDN from a dict
lbdn_from_dict = LBDN.from_dict(lbdn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


