# ApplicationCriterion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**name** | **str** | Name for the application. Since the name of application is unique it may be used as alternate key for the application. The &#39;name&#39; is used for import-export workflow and should be resolved to the &#39;id&#39; before continue processing Create/Update operations. | [optional] 
**subcategory** | **str** |  | [optional] 

## Example

```python
from fw.models.application_criterion import ApplicationCriterion

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCriterion from a JSON string
application_criterion_instance = ApplicationCriterion.from_json(json)
# print the JSON string representation of the object
print(ApplicationCriterion.to_json())

# convert the object into a dict
application_criterion_dict = application_criterion_instance.to_dict()
# create an instance of ApplicationCriterion from a dict
application_criterion_from_dict = ApplicationCriterion.from_dict(application_criterion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


