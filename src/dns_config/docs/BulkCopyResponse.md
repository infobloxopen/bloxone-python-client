# BulkCopyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[BulkCopyError]**](BulkCopyError.md) |  | [optional] 
**results** | [**List[CopyResponse]**](CopyResponse.md) |  | [optional] 

## Example

```python
from dns_config.models.bulk_copy_response import BulkCopyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCopyResponse from a JSON string
bulk_copy_response_instance = BulkCopyResponse.from_json(json)
# print the JSON string representation of the object
print(BulkCopyResponse.to_json())

# convert the object into a dict
bulk_copy_response_dict = bulk_copy_response_instance.to_dict()
# create an instance of BulkCopyResponse from a dict
bulk_copy_response_from_dict = BulkCopyResponse.from_dict(bulk_copy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


