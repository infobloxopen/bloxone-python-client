# HostInheritance

Inheritance configuration specifies how and which fields _Host_ object inherits from _Global_ or _Server_ parent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kerberos_keys** | [**InheritedKerberosKeys**](InheritedKerberosKeys.md) | Optional. Field config for _kerberos_keys_ field from _Host_ object. | [optional] 

## Example

```python
from dns_config.models.host_inheritance import HostInheritance

# TODO update the JSON string below
json = "{}"
# create an instance of HostInheritance from a JSON string
host_inheritance_instance = HostInheritance.from_json(json)
# print the JSON string representation of the object
print(HostInheritance.to_json())

# convert the object into a dict
host_inheritance_dict = host_inheritance_instance.to_dict()
# create an instance of HostInheritance from a dict
host_inheritance_from_dict = HostInheritance.from_dict(host_inheritance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


