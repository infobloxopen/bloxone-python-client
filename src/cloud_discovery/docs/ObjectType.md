# ObjectType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discover_new** | **bool** |  | [optional] 
**objects** | [**List[Object]**](Object.md) |  | [optional] 
**version** | **float** |  | [optional] 

## Example

```python
from cloud_discovery.models.object_type import ObjectType

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectType from a JSON string
object_type_instance = ObjectType.from_json(json)
# print the JSON string representation of the object
print(ObjectType.to_json())

# convert the object into a dict
object_type_dict = object_type_instance.to_dict()
# create an instance of ObjectType from a dict
object_type_from_dict = ObjectType.from_dict(object_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


