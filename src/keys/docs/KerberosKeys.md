# KerberosKeys

The list of __Key__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[KerberosKey]**](KerberosKey.md) |  | [optional] 

## Example

```python
from keys.models.kerberos_keys import KerberosKeys

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosKeys from a JSON string
kerberos_keys_instance = KerberosKeys.from_json(json)
# print the JSON string representation of the object
print(KerberosKeys.to_json())

# convert the object into a dict
kerberos_keys_dict = kerberos_keys_instance.to_dict()
# create an instance of KerberosKeys from a dict
kerberos_keys_from_dict = KerberosKeys.from_dict(kerberos_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


