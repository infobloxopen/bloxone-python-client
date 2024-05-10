# TypesJSONValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 

## Example

```python
from infra_provision.models.types_json_value import TypesJSONValue

# TODO update the JSON string below
json = "{}"
# create an instance of TypesJSONValue from a JSON string
types_json_value_instance = TypesJSONValue.from_json(json)
# print the JSON string representation of the object
print(TypesJSONValue.to_json())

# convert the object into a dict
types_json_value_dict = types_json_value_instance.to_dict()
# create an instance of TypesJSONValue from a dict
types_json_value_from_dict = TypesJSONValue.from_dict(types_json_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


