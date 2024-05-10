# UpdateForwardZoneResponse

The Forward Zone object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ForwardZone**](ForwardZone.md) |  | [optional] 

## Example

```python
from dns_config.models.update_forward_zone_response import UpdateForwardZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateForwardZoneResponse from a JSON string
update_forward_zone_response_instance = UpdateForwardZoneResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateForwardZoneResponse.to_json())

# convert the object into a dict
update_forward_zone_response_dict = update_forward_zone_response_instance.to_dict()
# create an instance of UpdateForwardZoneResponse from a dict
update_forward_zone_response_from_dict = UpdateForwardZoneResponse.from_dict(update_forward_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


