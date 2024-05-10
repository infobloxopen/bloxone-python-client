# KerberosKey

A __Key__ object represents a Kerberos key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Encryption algorithm of the key in accordance with RFC 3961. | [optional] [readonly] 
**comment** | **str** | The description for Kerberos key. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**domain** | **str** | Kerberos realm of the principal. | [optional] [readonly] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**principal** | **str** | Kerberos principal associated with key. | [optional] [readonly] 
**tags** | **object** | The tags for the Kerberos key in JSON format. | [optional] 
**uploaded_at** | **str** | Upload time for the key. | [optional] [readonly] 
**version** | **int** | The version number (KVNO) of the key. | [optional] [readonly] 

## Example

```python
from keys.models.kerberos_key import KerberosKey

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosKey from a JSON string
kerberos_key_instance = KerberosKey.from_json(json)
# print the JSON string representation of the object
print(KerberosKey.to_json())

# convert the object into a dict
kerberos_key_dict = kerberos_key_instance.to_dict()
# create an instance of KerberosKey from a dict
kerberos_key_from_dict = KerberosKey.from_dict(kerberos_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


