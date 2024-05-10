# BulkCopyError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the resource that was requested to be copied. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**message** | **str** | The reason why the copy failed. | [optional] 

## Example

```python
from ipam.models.bulk_copy_error import BulkCopyError

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCopyError from a JSON string
bulk_copy_error_instance = BulkCopyError.from_json(json)
# print the JSON string representation of the object
print(BulkCopyError.to_json())

# convert the object into a dict
bulk_copy_error_dict = bulk_copy_error_instance.to_dict()
# create an instance of BulkCopyError from a dict
bulk_copy_error_from_dict = BulkCopyError.from_dict(bulk_copy_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


