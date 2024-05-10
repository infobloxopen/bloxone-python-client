# UpdateHostResponse

The DNS Host object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Host**](Host.md) |  | [optional] 

## Example

```python
from dns_config.models.update_host_response import UpdateHostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHostResponse from a JSON string
update_host_response_instance = UpdateHostResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateHostResponse.to_json())

# convert the object into a dict
update_host_response_dict = update_host_response_instance.to_dict()
# create an instance of UpdateHostResponse from a dict
update_host_response_from_dict = UpdateHostResponse.from_dict(update_host_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


