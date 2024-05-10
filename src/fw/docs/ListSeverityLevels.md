# ListSeverityLevels

The Payload for Patch Operation to update Threat/Confidence Levels and Tags in TI List

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence_level** | **str** | The confidence level for a TI list. The possible values are [LOW\&quot;, \&quot;MEDIUM\&quot;, \&quot;HIGH\&quot;] | [optional] 
**id** | **int** | The Named List object identifier. | [optional] [readonly] 
**tags** | **object** | Enables tag support for resource where tags attribute contains user-defined key value pairs | [optional] 
**threat_level** | **str** | The threat level for a TI list. The possible values are [\&quot;INFO\&quot;, \&quot;LOW\&quot;, \&quot;MEDIUM\&quot;, \&quot;HIGH\&quot;] | [optional] 

## Example

```python
from fw.models.list_severity_levels import ListSeverityLevels

# TODO update the JSON string below
json = "{}"
# create an instance of ListSeverityLevels from a JSON string
list_severity_levels_instance = ListSeverityLevels.from_json(json)
# print the JSON string representation of the object
print(ListSeverityLevels.to_json())

# convert the object into a dict
list_severity_levels_dict = list_severity_levels_instance.to_dict()
# create an instance of ListSeverityLevels from a dict
list_severity_levels_from_dict = ListSeverityLevels.from_dict(list_severity_levels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


