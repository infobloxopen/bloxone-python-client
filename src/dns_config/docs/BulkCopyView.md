# BulkCopyView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_zone_config** | [**AuthZoneConfig**](AuthZoneConfig.md) |  | [optional] 
**forward_zone_config** | [**ForwardZoneConfig**](ForwardZoneConfig.md) |  | [optional] 
**recursive** | **bool** | Indicates whether child objects should be copied or not.  Defaults to _false_. Reserved for future use. | [optional] 
**resources** | **List[str]** | The resource identifier. | 
**secondary_zone_config** | [**AuthZoneConfig**](AuthZoneConfig.md) |  | [optional] 
**skip_on_error** | **bool** | Indicates whether copying should skip object in case of error and continue with next, or abort copying in case of error.  Defaults to _false_. | [optional] 
**target** | **str** | The resource identifier. | 

## Example

```python
from dns_config.models.bulk_copy_view import BulkCopyView

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCopyView from a JSON string
bulk_copy_view_instance = BulkCopyView.from_json(json)
# print the JSON string representation of the object
print(BulkCopyView.to_json())

# convert the object into a dict
bulk_copy_view_dict = bulk_copy_view_instance.to_dict()
# create an instance of BulkCopyView from a dict
bulk_copy_view_from_dict = BulkCopyView.from_dict(bulk_copy_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


