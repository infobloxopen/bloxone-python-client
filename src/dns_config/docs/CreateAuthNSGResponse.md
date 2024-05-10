# CreateAuthNSGResponse

The AuthNSG object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**AuthNSG**](AuthNSG.md) |  | [optional] 

## Example

```python
from dns_config.models.create_auth_nsg_response import CreateAuthNSGResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthNSGResponse from a JSON string
create_auth_nsg_response_instance = CreateAuthNSGResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAuthNSGResponse.to_json())

# convert the object into a dict
create_auth_nsg_response_dict = create_auth_nsg_response_instance.to_dict()
# create an instance of CreateAuthNSGResponse from a dict
create_auth_nsg_response_from_dict = CreateAuthNSGResponse.from_dict(create_auth_nsg_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


