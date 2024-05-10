# HostName

The __HostName__ object represents a name associated with the __Host__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **bool** | When _true_, the name is treated as an alias. | [optional] 
**name** | **str** | A name for the host. | 
**primary_name** | **bool** | When _true_, the name field is treated as primary name. There must be one and only one primary name in the list of host names. The primary name will be treated as the canonical name for all the aliases. PTR record will be generated only for the primary name. | [optional] 
**zone** | **str** | The resource identifier. | 

## Example

```python
from ipam.models.host_name import HostName

# TODO update the JSON string below
json = "{}"
# create an instance of HostName from a JSON string
host_name_instance = HostName.from_json(json)
# print the JSON string representation of the object
print(HostName.to_json())

# convert the object into a dict
host_name_dict = host_name_instance.to_dict()
# create an instance of HostName from a dict
host_name_from_dict = HostName.from_dict(host_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


