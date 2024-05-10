# AnycastVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from anycast.models.anycast_version import AnycastVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AnycastVersion from a JSON string
anycast_version_instance = AnycastVersion.from_json(json)
# print the JSON string representation of the object
print(AnycastVersion.to_json())

# convert the object into a dict
anycast_version_dict = anycast_version_instance.to_dict()
# create an instance of AnycastVersion from a dict
anycast_version_from_dict = AnycastVersion.from_dict(anycast_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


