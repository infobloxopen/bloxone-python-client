# ReadKerberosKeyResponse

The response format to retrieve the __KerberosKey__ resource extracted from the uploaded keytab file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**KerberosKey**](KerberosKey.md) | The __KerberosKey__ object. | [optional] 

## Example

```python
from keys.models.read_kerberos_key_response import ReadKerberosKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadKerberosKeyResponse from a JSON string
read_kerberos_key_response_instance = ReadKerberosKeyResponse.from_json(json)
# print the JSON string representation of the object
print(ReadKerberosKeyResponse.to_json())

# convert the object into a dict
read_kerberos_key_response_dict = read_kerberos_key_response_instance.to_dict()
# create an instance of ReadKerberosKeyResponse from a dict
read_kerberos_key_response_from_dict = ReadKerberosKeyResponse.from_dict(read_kerberos_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


