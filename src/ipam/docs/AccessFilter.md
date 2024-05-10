# AccessFilter

The __AccessFilter__ object represents an allow/deny filter for a DHCP range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** | The access type of DHCP filter (_allow_ or _deny_).  Defaults to _allow_. | 
**hardware_filter_id** | **str** | The resource identifier. | [optional] 
**option_filter_id** | **str** | The resource identifier. | [optional] 

## Example

```python
from ipam.models.access_filter import AccessFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AccessFilter from a JSON string
access_filter_instance = AccessFilter.from_json(json)
# print the JSON string representation of the object
print(AccessFilter.to_json())

# convert the object into a dict
access_filter_dict = access_filter_instance.to_dict()
# create an instance of AccessFilter from a dict
access_filter_from_dict = AccessFilter.from_dict(access_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


