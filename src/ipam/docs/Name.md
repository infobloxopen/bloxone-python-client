# Name

The __Name__ object represents a name associated with an address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name expressed as a single label or FQDN. | 
**type** | **str** | The origin of the name. | 

## Example

```python
from ipam.models.name import Name

# TODO update the JSON string below
json = "{}"
# create an instance of Name from a JSON string
name_instance = Name.from_json(json)
# print the JSON string representation of the object
print(Name.to_json())

# convert the object into a dict
name_dict = name_instance.to_dict()
# create an instance of Name from a dict
name_from_dict = Name.from_dict(name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


