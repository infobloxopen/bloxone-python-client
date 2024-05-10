# CreateTSIGKeyResponse

The response format to create a __TSIGKey__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**TSIGKey**](TSIGKey.md) |  | [optional] 

## Example

```python
from keys.models.create_tsig_key_response import CreateTSIGKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTSIGKeyResponse from a JSON string
create_tsig_key_response_instance = CreateTSIGKeyResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTSIGKeyResponse.to_json())

# convert the object into a dict
create_tsig_key_response_dict = create_tsig_key_response_instance.to_dict()
# create an instance of CreateTSIGKeyResponse from a dict
create_tsig_key_response_from_dict = CreateTSIGKeyResponse.from_dict(create_tsig_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


