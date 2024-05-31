# CreateAuthZoneResponse

The Authoritative Zone object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**AuthZone**](AuthZone.md) | The created AuthZone object. | [optional] 

## Example

```python
from dns_config.models.create_auth_zone_response import CreateAuthZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthZoneResponse from a JSON string
create_auth_zone_response_instance = CreateAuthZoneResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAuthZoneResponse.to_json())

# convert the object into a dict
create_auth_zone_response_dict = create_auth_zone_response_instance.to_dict()
# create an instance of CreateAuthZoneResponse from a dict
create_auth_zone_response_from_dict = CreateAuthZoneResponse.from_dict(create_auth_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


