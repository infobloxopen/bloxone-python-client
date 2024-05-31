# UpdateKerberosKeyResponse

The response format to update __KerberosKey__ resource extracted from the uploaded keytab file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**KerberosKey**](KerberosKey.md) | The __KerberosKey__ object. | [optional] 

## Example

```python
from keys.models.update_kerberos_key_response import UpdateKerberosKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKerberosKeyResponse from a JSON string
update_kerberos_key_response_instance = UpdateKerberosKeyResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateKerberosKeyResponse.to_json())

# convert the object into a dict
update_kerberos_key_response_dict = update_kerberos_key_response_instance.to_dict()
# create an instance of UpdateKerberosKeyResponse from a dict
update_kerberos_key_response_from_dict = UpdateKerberosKeyResponse.from_dict(update_kerberos_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


