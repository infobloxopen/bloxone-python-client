# UpdateGlobalResponse

The Global object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**DNSGlobal**](DNSGlobal.md) |  | [optional] 

## Example

```python
from dns_config.models.update_global_response import UpdateGlobalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGlobalResponse from a JSON string
update_global_response_instance = UpdateGlobalResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateGlobalResponse.to_json())

# convert the object into a dict
update_global_response_dict = update_global_response_instance.to_dict()
# create an instance of UpdateGlobalResponse from a dict
update_global_response_from_dict = UpdateGlobalResponse.from_dict(update_global_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


