# BulkCopyIPSpaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[BulkCopyError]**](BulkCopyError.md) |  | [optional] 
**results** | [**List[CopyResponse]**](CopyResponse.md) |  | [optional] 

## Example

```python
from ipam.models.bulk_copy_ip_space_response import BulkCopyIPSpaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCopyIPSpaceResponse from a JSON string
bulk_copy_ip_space_response_instance = BulkCopyIPSpaceResponse.from_json(json)
# print the JSON string representation of the object
print(BulkCopyIPSpaceResponse.to_json())

# convert the object into a dict
bulk_copy_ip_space_response_dict = bulk_copy_ip_space_response_instance.to_dict()
# create an instance of BulkCopyIPSpaceResponse from a dict
bulk_copy_ip_space_response_from_dict = BulkCopyIPSpaceResponse.from_dict(bulk_copy_ip_space_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


