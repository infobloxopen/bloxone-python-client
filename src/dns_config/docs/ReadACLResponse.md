# ReadACLResponse

The ACL object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ACL**](ACL.md) | The ACL object. | [optional] 

## Example

```python
from dns_config.models.read_acl_response import ReadACLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadACLResponse from a JSON string
read_acl_response_instance = ReadACLResponse.from_json(json)
# print the JSON string representation of the object
print(ReadACLResponse.to_json())

# convert the object into a dict
read_acl_response_dict = read_acl_response_instance.to_dict()
# create an instance of ReadACLResponse from a dict
read_acl_response_from_dict = ReadACLResponse.from_dict(read_acl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


