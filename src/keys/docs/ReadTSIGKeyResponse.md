# ReadTSIGKeyResponse

The response format to retrieve the __TSIGKey__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**TSIGKey**](TSIGKey.md) | The TSIGKey object. | [optional] 

## Example

```python
from keys.models.read_tsig_key_response import ReadTSIGKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadTSIGKeyResponse from a JSON string
read_tsig_key_response_instance = ReadTSIGKeyResponse.from_json(json)
# print the JSON string representation of the object
print(ReadTSIGKeyResponse.to_json())

# convert the object into a dict
read_tsig_key_response_dict = read_tsig_key_response_instance.to_dict()
# create an instance of ReadTSIGKeyResponse from a dict
read_tsig_key_response_from_dict = ReadTSIGKeyResponse.from_dict(read_tsig_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


