# ListKerberosKeyResponse

The response format to retrieve __KerberosKey__ resources extracted from the uploaded keytab file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[KerberosKey]**](KerberosKey.md) | The list of KerberosKey objects. | [optional] 

## Example

```python
from keys.models.list_kerberos_key_response import ListKerberosKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListKerberosKeyResponse from a JSON string
list_kerberos_key_response_instance = ListKerberosKeyResponse.from_json(json)
# print the JSON string representation of the object
print(ListKerberosKeyResponse.to_json())

# convert the object into a dict
list_kerberos_key_response_dict = list_kerberos_key_response_instance.to_dict()
# create an instance of ListKerberosKeyResponse from a dict
list_kerberos_key_response_from_dict = ListKerberosKeyResponse.from_dict(list_kerberos_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


