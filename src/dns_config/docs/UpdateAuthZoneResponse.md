# UpdateAuthZoneResponse

The Authoritative Zone object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**AuthZone**](AuthZone.md) |  | [optional] 

## Example

```python
from dns_config.models.update_auth_zone_response import UpdateAuthZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAuthZoneResponse from a JSON string
update_auth_zone_response_instance = UpdateAuthZoneResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAuthZoneResponse.to_json())

# convert the object into a dict
update_auth_zone_response_dict = update_auth_zone_response_instance.to_dict()
# create an instance of UpdateAuthZoneResponse from a dict
update_auth_zone_response_from_dict = UpdateAuthZoneResponse.from_dict(update_auth_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


