# TypesConfigCheckRequest

The Config Check request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**config_check_type** | **str** |  | [optional] 
**notify** | **bool** | Caller sets to false if wants to suppress notification. | [optional] 

## Example

```python
from dfp.models.types_config_check_request import TypesConfigCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TypesConfigCheckRequest from a JSON string
types_config_check_request_instance = TypesConfigCheckRequest.from_json(json)
# print the JSON string representation of the object
print(TypesConfigCheckRequest.to_json())

# convert the object into a dict
types_config_check_request_dict = types_config_check_request_instance.to_dict()
# create an instance of TypesConfigCheckRequest from a dict
types_config_check_request_from_dict = TypesConfigCheckRequest.from_dict(types_config_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


