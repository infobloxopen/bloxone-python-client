# ReadGlobalResponse

The Global object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**DNSGlobal**](DNSGlobal.md) | The global object. | [optional] 

## Example

```python
from dns_config.models.read_global_response import ReadGlobalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadGlobalResponse from a JSON string
read_global_response_instance = ReadGlobalResponse.from_json(json)
# print the JSON string representation of the object
print(ReadGlobalResponse.to_json())

# convert the object into a dict
read_global_response_dict = read_global_response_instance.to_dict()
# create an instance of ReadGlobalResponse from a dict
read_global_response_from_dict = ReadGlobalResponse.from_dict(read_global_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


