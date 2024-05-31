# CreateASMResponse

The response format to update subnet and range for ASM.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ASM**](ASM.md) | The ASM object. | [optional] 

## Example

```python
from ipam.models.create_asm_response import CreateASMResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateASMResponse from a JSON string
create_asm_response_instance = CreateASMResponse.from_json(json)
# print the JSON string representation of the object
print(CreateASMResponse.to_json())

# convert the object into a dict
create_asm_response_dict = create_asm_response_instance.to_dict()
# create an instance of CreateASMResponse from a dict
create_asm_response_from_dict = CreateASMResponse.from_dict(create_asm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


