# AccessCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | Auto generated unique Bypass Code value | [optional] 
**activation** | **datetime** | The time when the Bypass Code object was activated. | [optional] 
**created_time** | **datetime** | The time when the Bypass Code object was created. | [optional] [readonly] 
**description** | **str** |  | [optional] 
**expiration** | **datetime** | The time when the Bypass Code object was expired. | [optional] 
**name** | **str** | The name of Bypass Code | [optional] 
**policy_ids** | **List[int]** | The list of SecurityPolicy object identifiers. | [optional] 
**rules** | [**List[AccessCodeRule]**](AccessCodeRule.md) | The list of selected security rules | [optional] 
**updated_time** | **datetime** | The time when the Bypass Code object was last updated. | [optional] [readonly] 

## Example

```python
from fw.models.access_code import AccessCode

# TODO update the JSON string below
json = "{}"
# create an instance of AccessCode from a JSON string
access_code_instance = AccessCode.from_json(json)
# print the JSON string representation of the object
print(AccessCode.to_json())

# convert the object into a dict
access_code_dict = access_code_instance.to_dict()
# create an instance of AccessCode from a dict
access_code_from_dict = AccessCode.from_dict(access_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


