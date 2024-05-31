# UpdateAuthNSGResponse

The AuthNSG object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**AuthNSG**](AuthNSG.md) | The updated AuthNSG object. | [optional] 

## Example

```python
from dns_config.models.update_auth_nsg_response import UpdateAuthNSGResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAuthNSGResponse from a JSON string
update_auth_nsg_response_instance = UpdateAuthNSGResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAuthNSGResponse.to_json())

# convert the object into a dict
update_auth_nsg_response_dict = update_auth_nsg_response_instance.to_dict()
# create an instance of UpdateAuthNSGResponse from a dict
update_auth_nsg_response_from_dict = UpdateAuthNSGResponse.from_dict(update_auth_nsg_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


