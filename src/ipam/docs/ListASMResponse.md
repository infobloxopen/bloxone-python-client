# ListASMResponse

The response format to retrieve __ASM__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ASM]**](ASM.md) | The list of ASM objects. | [optional] 

## Example

```python
from ipam.models.list_asm_response import ListASMResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListASMResponse from a JSON string
list_asm_response_instance = ListASMResponse.from_json(json)
# print the JSON string representation of the object
print(ListASMResponse.to_json())

# convert the object into a dict
list_asm_response_dict = list_asm_response_instance.to_dict()
# create an instance of ListASMResponse from a dict
list_asm_response_from_dict = ListASMResponse.from_dict(list_asm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


