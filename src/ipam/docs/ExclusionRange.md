# ExclusionRange

The __ExclusionRange__ object represents an exclusion range inside a DHCP range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The description for the exclusion range. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**end** | **str** | The end address of the exclusion range. | 
**start** | **str** | The start address of the exclusion range. | 

## Example

```python
from ipam.models.exclusion_range import ExclusionRange

# TODO update the JSON string below
json = "{}"
# create an instance of ExclusionRange from a JSON string
exclusion_range_instance = ExclusionRange.from_json(json)
# print the JSON string representation of the object
print(ExclusionRange.to_json())

# convert the object into a dict
exclusion_range_dict = exclusion_range_instance.to_dict()
# create an instance of ExclusionRange from a dict
exclusion_range_from_dict = ExclusionRange.from_dict(exclusion_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


