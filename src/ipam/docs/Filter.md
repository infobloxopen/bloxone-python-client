# Filter

A DHCP Filter (_dhcp/filter_) object lists DHCP filters of all types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The description for the DHCP filter. May contain 0 to 1024 characters. Can include UTF-8. | [optional] [readonly] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The name of the DHCP filter. | [optional] [readonly] 
**protocol** | **str** | The type of protocol of the filter (_ip4_ or _ip6_). | [optional] [readonly] 
**role** | **str** | The role of DHCP filter (_values_ or _selection_). | [optional] 
**tags** | **object** | The tags for the DHCP filter in JSON format. | [optional] 
**type** | **str** | The type of DHCP filter (_hardware_ or _option_). | [optional] [readonly] 

## Example

```python
from ipam.models.filter import Filter

# TODO update the JSON string below
json = "{}"
# create an instance of Filter from a JSON string
filter_instance = Filter.from_json(json)
# print the JSON string representation of the object
print(Filter.to_json())

# convert the object into a dict
filter_dict = filter_instance.to_dict()
# create an instance of Filter from a dict
filter_from_dict = Filter.from_dict(filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


