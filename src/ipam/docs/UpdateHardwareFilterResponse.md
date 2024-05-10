# UpdateHardwareFilterResponse

The response format to update the __HardwareFilter__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**HardwareFilter**](HardwareFilter.md) |  | [optional] 

## Example

```python
from ipam.models.update_hardware_filter_response import UpdateHardwareFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHardwareFilterResponse from a JSON string
update_hardware_filter_response_instance = UpdateHardwareFilterResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateHardwareFilterResponse.to_json())

# convert the object into a dict
update_hardware_filter_response_dict = update_hardware_filter_response_instance.to_dict()
# create an instance of UpdateHardwareFilterResponse from a dict
update_hardware_filter_response_from_dict = UpdateHardwareFilterResponse.from_dict(update_hardware_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


