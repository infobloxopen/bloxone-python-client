# ReadForwardZoneResponse

The Forward Zone object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ForwardZone**](ForwardZone.md) |  | [optional] 

## Example

```python
from dns_config.models.read_forward_zone_response import ReadForwardZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadForwardZoneResponse from a JSON string
read_forward_zone_response_instance = ReadForwardZoneResponse.from_json(json)
# print the JSON string representation of the object
print(ReadForwardZoneResponse.to_json())

# convert the object into a dict
read_forward_zone_response_dict = read_forward_zone_response_instance.to_dict()
# create an instance of ReadForwardZoneResponse from a dict
read_forward_zone_response_from_dict = ReadForwardZoneResponse.from_dict(read_forward_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


