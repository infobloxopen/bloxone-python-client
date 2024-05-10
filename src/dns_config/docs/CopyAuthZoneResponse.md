# CopyAuthZoneResponse

The Authoritative Zone object copy response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CopyResponse**](CopyResponse.md) |  | [optional] 

## Example

```python
from dns_config.models.copy_auth_zone_response import CopyAuthZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CopyAuthZoneResponse from a JSON string
copy_auth_zone_response_instance = CopyAuthZoneResponse.from_json(json)
# print the JSON string representation of the object
print(CopyAuthZoneResponse.to_json())

# convert the object into a dict
copy_auth_zone_response_dict = copy_auth_zone_response_instance.to_dict()
# create an instance of CopyAuthZoneResponse from a dict
copy_auth_zone_response_from_dict = CopyAuthZoneResponse.from_dict(copy_auth_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


