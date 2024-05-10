# ListForwardZoneResponse

The Forward Zone objects list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ForwardZone]**](ForwardZone.md) | List of Forward Zone objects. | [optional] 

## Example

```python
from dns_config.models.list_forward_zone_response import ListForwardZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListForwardZoneResponse from a JSON string
list_forward_zone_response_instance = ListForwardZoneResponse.from_json(json)
# print the JSON string representation of the object
print(ListForwardZoneResponse.to_json())

# convert the object into a dict
list_forward_zone_response_dict = list_forward_zone_response_instance.to_dict()
# create an instance of ListForwardZoneResponse from a dict
list_forward_zone_response_from_dict = ListForwardZoneResponse.from_dict(list_forward_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


