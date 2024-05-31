# ReadAuthNSGResponse

The AuthNSG object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**AuthNSG**](AuthNSG.md) | The AuthNSG object. | [optional] 

## Example

```python
from dns_config.models.read_auth_nsg_response import ReadAuthNSGResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadAuthNSGResponse from a JSON string
read_auth_nsg_response_instance = ReadAuthNSGResponse.from_json(json)
# print the JSON string representation of the object
print(ReadAuthNSGResponse.to_json())

# convert the object into a dict
read_auth_nsg_response_dict = read_auth_nsg_response_instance.to_dict()
# create an instance of ReadAuthNSGResponse from a dict
read_auth_nsg_response_from_dict = ReadAuthNSGResponse.from_dict(read_auth_nsg_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


