# ListAuthZoneResponse

The Authoritative Zone object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AuthZone]**](AuthZone.md) | The list of Auth Zone objects. | [optional] 

## Example

```python
from dns_config.models.list_auth_zone_response import ListAuthZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAuthZoneResponse from a JSON string
list_auth_zone_response_instance = ListAuthZoneResponse.from_json(json)
# print the JSON string representation of the object
print(ListAuthZoneResponse.to_json())

# convert the object into a dict
list_auth_zone_response_dict = list_auth_zone_response_instance.to_dict()
# create an instance of ListAuthZoneResponse from a dict
list_auth_zone_response_from_dict = ListAuthZoneResponse.from_dict(list_auth_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


