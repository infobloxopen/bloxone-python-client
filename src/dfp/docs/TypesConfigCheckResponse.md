# TypesConfigCheckResponse

The Config Check response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[TypesConfigCheckResult]**](TypesConfigCheckResult.md) | The list of check result. | [optional] 

## Example

```python
from dfp.models.types_config_check_response import TypesConfigCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TypesConfigCheckResponse from a JSON string
types_config_check_response_instance = TypesConfigCheckResponse.from_json(json)
# print the JSON string representation of the object
print(TypesConfigCheckResponse.to_json())

# convert the object into a dict
types_config_check_response_dict = types_config_check_response_instance.to_dict()
# create an instance of TypesConfigCheckResponse from a dict
types_config_check_response_from_dict = TypesConfigCheckResponse.from_dict(types_config_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


