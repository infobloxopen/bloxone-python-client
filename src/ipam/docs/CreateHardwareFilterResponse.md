# CreateHardwareFilterResponse

The response format to create the __HardwareFilter__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**HardwareFilter**](HardwareFilter.md) |  | [optional] 

## Example

```python
from ipam.models.create_hardware_filter_response import CreateHardwareFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHardwareFilterResponse from a JSON string
create_hardware_filter_response_instance = CreateHardwareFilterResponse.from_json(json)
# print the JSON string representation of the object
print(CreateHardwareFilterResponse.to_json())

# convert the object into a dict
create_hardware_filter_response_dict = create_hardware_filter_response_instance.to_dict()
# create an instance of CreateHardwareFilterResponse from a dict
create_hardware_filter_response_from_dict = CreateHardwareFilterResponse.from_dict(create_hardware_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


