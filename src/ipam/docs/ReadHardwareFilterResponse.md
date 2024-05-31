# ReadHardwareFilterResponse

The response format to retrieve the __HardwareFilter__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**HardwareFilter**](HardwareFilter.md) | The HardwareFilter object. | [optional] 

## Example

```python
from ipam.models.read_hardware_filter_response import ReadHardwareFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadHardwareFilterResponse from a JSON string
read_hardware_filter_response_instance = ReadHardwareFilterResponse.from_json(json)
# print the JSON string representation of the object
print(ReadHardwareFilterResponse.to_json())

# convert the object into a dict
read_hardware_filter_response_dict = read_hardware_filter_response_instance.to_dict()
# create an instance of ReadHardwareFilterResponse from a dict
read_hardware_filter_response_from_dict = ReadHardwareFilterResponse.from_dict(read_hardware_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


