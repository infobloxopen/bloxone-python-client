# ApplicationFilter

The Application Filter object.  Application filters are content application rules that Infoblox Cloud uses to detect and filter specific internet content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **datetime** | The time when this Application Filter object was created. | [optional] [readonly] 
**criteria** | [**List[ApplicationCriterion]**](ApplicationCriterion.md) | The array of key-value pairs specifying criteria for the search. | [optional] 
**description** | **str** | The brief description for the application filter. | [optional] 
**id** | **int** | The Application Filter object identifier. | [optional] [readonly] 
**name** | **str** | The name of the application filter. | [optional] 
**policies** | **List[str]** | The list of security policy names with which the application filter is associated. | [optional] [readonly] 
**readonly** | **bool** | True if it is a predefined application filter | [optional] 
**tags** | **object** | Enables tag support for resource where tags attribute contains user-defined key value pairs | [optional] 
**updated_time** | **datetime** | The time when this Application Filter object was last updated. | [optional] [readonly] 

## Example

```python
from fw.models.application_filter import ApplicationFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFilter from a JSON string
application_filter_instance = ApplicationFilter.from_json(json)
# print the JSON string representation of the object
print(ApplicationFilter.to_json())

# convert the object into a dict
application_filter_dict = application_filter_instance.to_dict()
# create an instance of ApplicationFilter from a dict
application_filter_from_dict = ApplicationFilter.from_dict(application_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


