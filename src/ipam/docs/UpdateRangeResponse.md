# UpdateRangeResponse

The response format to update the __Range__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Range**](Range.md) | The Range object. | [optional] 

## Example

```python
from ipam.models.update_range_response import UpdateRangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRangeResponse from a JSON string
update_range_response_instance = UpdateRangeResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateRangeResponse.to_json())

# convert the object into a dict
update_range_response_dict = update_range_response_instance.to_dict()
# create an instance of UpdateRangeResponse from a dict
update_range_response_from_dict = UpdateRangeResponse.from_dict(update_range_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


