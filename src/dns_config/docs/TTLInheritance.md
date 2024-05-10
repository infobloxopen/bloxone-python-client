# TTLInheritance

The inheritance configuration specifies how the object inherits the _ttl_ field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 

## Example

```python
from dns_config.models.ttl_inheritance import TTLInheritance

# TODO update the JSON string below
json = "{}"
# create an instance of TTLInheritance from a JSON string
ttl_inheritance_instance = TTLInheritance.from_json(json)
# print the JSON string representation of the object
print(TTLInheritance.to_json())

# convert the object into a dict
ttl_inheritance_dict = ttl_inheritance_instance.to_dict()
# create an instance of TTLInheritance from a dict
ttl_inheritance_from_dict = TTLInheritance.from_dict(ttl_inheritance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


