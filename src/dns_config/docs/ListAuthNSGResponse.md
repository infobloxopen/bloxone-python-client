# ListAuthNSGResponse

The AuthNSG object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AuthNSG]**](AuthNSG.md) | List of AuthNSG objects. | [optional] 

## Example

```python
from dns_config.models.list_auth_nsg_response import ListAuthNSGResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAuthNSGResponse from a JSON string
list_auth_nsg_response_instance = ListAuthNSGResponse.from_json(json)
# print the JSON string representation of the object
print(ListAuthNSGResponse.to_json())

# convert the object into a dict
list_auth_nsg_response_dict = list_auth_nsg_response_instance.to_dict()
# create an instance of ListAuthNSGResponse from a dict
list_auth_nsg_response_from_dict = ListAuthNSGResponse.from_dict(list_auth_nsg_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


