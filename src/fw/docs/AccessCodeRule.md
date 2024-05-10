# AccessCodeRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**redirect_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from fw.models.access_code_rule import AccessCodeRule

# TODO update the JSON string below
json = "{}"
# create an instance of AccessCodeRule from a JSON string
access_code_rule_instance = AccessCodeRule.from_json(json)
# print the JSON string representation of the object
print(AccessCodeRule.to_json())

# convert the object into a dict
access_code_rule_dict = access_code_rule_instance.to_dict()
# create an instance of AccessCodeRule from a dict
access_code_rule_from_dict = AccessCodeRule.from_dict(access_code_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


