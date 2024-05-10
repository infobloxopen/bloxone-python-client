# RecordInheritance

The inheritance configuration specifies how the _Record_ object inherits the _ttl_ field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) |  | [optional] 

## Example

```python
from dns_data.models.record_inheritance import RecordInheritance

# TODO update the JSON string below
json = "{}"
# create an instance of RecordInheritance from a JSON string
record_inheritance_instance = RecordInheritance.from_json(json)
# print the JSON string representation of the object
print(RecordInheritance.to_json())

# convert the object into a dict
record_inheritance_dict = record_inheritance_instance.to_dict()
# create an instance of RecordInheritance from a dict
record_inheritance_from_dict = RecordInheritance.from_dict(record_inheritance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


