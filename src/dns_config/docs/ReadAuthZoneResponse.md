# ReadAuthZoneResponse

The Authoritative Zone object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**AuthZone**](AuthZone.md) | The AuthZone object. | [optional] 

## Example

```python
from dns_config.models.read_auth_zone_response import ReadAuthZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadAuthZoneResponse from a JSON string
read_auth_zone_response_instance = ReadAuthZoneResponse.from_json(json)
# print the JSON string representation of the object
print(ReadAuthZoneResponse.to_json())

# convert the object into a dict
read_auth_zone_response_dict = read_auth_zone_response_instance.to_dict()
# create an instance of ReadAuthZoneResponse from a dict
read_auth_zone_response_from_dict = ReadAuthZoneResponse.from_dict(read_auth_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


