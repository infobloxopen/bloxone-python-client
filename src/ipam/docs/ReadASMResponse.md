# ReadASMResponse

The response format to retrieve the __ASM__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ASM**](ASM.md) | The ASM object. | [optional] 

## Example

```python
from ipam.models.read_asm_response import ReadASMResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadASMResponse from a JSON string
read_asm_response_instance = ReadASMResponse.from_json(json)
# print the JSON string representation of the object
print(ReadASMResponse.to_json())

# convert the object into a dict
read_asm_response_dict = read_asm_response_instance.to_dict()
# create an instance of ReadASMResponse from a dict
read_asm_response_from_dict = ReadASMResponse.from_dict(read_asm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


