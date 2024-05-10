# ServiceConfigObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_body** | **bytearray** |  | [optional] 
**ophid** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from anycast.models.service_config_object import ServiceConfigObject

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConfigObject from a JSON string
service_config_object_instance = ServiceConfigObject.from_json(json)
# print the JSON string representation of the object
print(ServiceConfigObject.to_json())

# convert the object into a dict
service_config_object_dict = service_config_object_instance.to_dict()
# create an instance of ServiceConfigObject from a dict
service_config_object_from_dict = ServiceConfigObject.from_dict(service_config_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


