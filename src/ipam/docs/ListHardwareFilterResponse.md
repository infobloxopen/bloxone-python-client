# ListHardwareFilterResponse

The response format to retrieve __HardwareFilter__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[HardwareFilter]**](HardwareFilter.md) | The list of HardwareFilter objects. | [optional] 

## Example

```python
from ipam.models.list_hardware_filter_response import ListHardwareFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListHardwareFilterResponse from a JSON string
list_hardware_filter_response_instance = ListHardwareFilterResponse.from_json(json)
# print the JSON string representation of the object
print(ListHardwareFilterResponse.to_json())

# convert the object into a dict
list_hardware_filter_response_dict = list_hardware_filter_response_instance.to_dict()
# create an instance of ListHardwareFilterResponse from a dict
list_hardware_filter_response_from_dict = ListHardwareFilterResponse.from_dict(list_hardware_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


