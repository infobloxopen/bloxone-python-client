# ListTSIGKeyResponse

The response format to retrieve __TSIGKey__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[TSIGKey]**](TSIGKey.md) | The list of TSIGKey objects. | [optional] 

## Example

```python
from keys.models.list_tsig_key_response import ListTSIGKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTSIGKeyResponse from a JSON string
list_tsig_key_response_instance = ListTSIGKeyResponse.from_json(json)
# print the JSON string representation of the object
print(ListTSIGKeyResponse.to_json())

# convert the object into a dict
list_tsig_key_response_dict = list_tsig_key_response_instance.to_dict()
# create an instance of ListTSIGKeyResponse from a dict
list_tsig_key_response_from_dict = ListTSIGKeyResponse.from_dict(list_tsig_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


