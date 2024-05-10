# UpdateACLResponse

The ACL object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ACL**](ACL.md) |  | [optional] 

## Example

```python
from dns_config.models.update_acl_response import UpdateACLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateACLResponse from a JSON string
update_acl_response_instance = UpdateACLResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateACLResponse.to_json())

# convert the object into a dict
update_acl_response_dict = update_acl_response_instance.to_dict()
# create an instance of UpdateACLResponse from a dict
update_acl_response_from_dict = UpdateACLResponse.from_dict(update_acl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


