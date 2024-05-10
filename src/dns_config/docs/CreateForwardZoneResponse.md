# CreateForwardZoneResponse

The Forward Zone object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ForwardZone**](ForwardZone.md) |  | [optional] 

## Example

```python
from dns_config.models.create_forward_zone_response import CreateForwardZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateForwardZoneResponse from a JSON string
create_forward_zone_response_instance = CreateForwardZoneResponse.from_json(json)
# print the JSON string representation of the object
print(CreateForwardZoneResponse.to_json())

# convert the object into a dict
create_forward_zone_response_dict = create_forward_zone_response_instance.to_dict()
# create an instance of CreateForwardZoneResponse from a dict
create_forward_zone_response_from_dict = CreateForwardZoneResponse.from_dict(create_forward_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


