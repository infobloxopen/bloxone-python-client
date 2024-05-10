# InheritedKerberosKeys

Inheritance configuration for a field of type list of _kerberos_key_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Optional. Inheritance setting for a field. Defaults to _inherit_. | [optional] 
**display_name** | **str** | Human-readable display name for the object referred to by _source_. | [optional] [readonly] 
**source** | **str** | The resource identifier. | [optional] [readonly] 
**value** | [**List[KerberosKey]**](KerberosKey.md) | Inherited value. | [optional] [readonly] 

## Example

```python
from dns_config.models.inherited_kerberos_keys import InheritedKerberosKeys

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedKerberosKeys from a JSON string
inherited_kerberos_keys_instance = InheritedKerberosKeys.from_json(json)
# print the JSON string representation of the object
print(InheritedKerberosKeys.to_json())

# convert the object into a dict
inherited_kerberos_keys_dict = inherited_kerberos_keys_instance.to_dict()
# create an instance of InheritedKerberosKeys from a dict
inherited_kerberos_keys_from_dict = InheritedKerberosKeys.from_dict(inherited_kerberos_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


