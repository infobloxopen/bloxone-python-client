# TypesConfigCheckResult

The ConfigCheckResult object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | **str** | Provides more info about the potential problem. | [optional] 
**config_check_type** | **str** | Service check type. | [optional] 
**resource_uri** | **str** | URI of the resource that was checked. | [optional] 
**result_code** | **str** | The check result. | [optional] 

## Example

```python
from dfp.models.types_config_check_result import TypesConfigCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of TypesConfigCheckResult from a JSON string
types_config_check_result_instance = TypesConfigCheckResult.from_json(json)
# print the JSON string representation of the object
print(TypesConfigCheckResult.to_json())

# convert the object into a dict
types_config_check_result_dict = types_config_check_result_instance.to_dict()
# create an instance of TypesConfigCheckResult from a dict
types_config_check_result_from_dict = TypesConfigCheckResult.from_dict(types_config_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


