# UpdateTSIGKeyResponse

The response format to update __TSIGKey__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**TSIGKey**](TSIGKey.md) | The TSIGKey object. | [optional] 

## Example

```python
from keys.models.update_tsig_key_response import UpdateTSIGKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTSIGKeyResponse from a JSON string
update_tsig_key_response_instance = UpdateTSIGKeyResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateTSIGKeyResponse.to_json())

# convert the object into a dict
update_tsig_key_response_dict = update_tsig_key_response_instance.to_dict()
# create an instance of UpdateTSIGKeyResponse from a dict
update_tsig_key_response_from_dict = UpdateTSIGKeyResponse.from_dict(update_tsig_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


