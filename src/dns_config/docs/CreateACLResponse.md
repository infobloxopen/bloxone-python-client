# CreateACLResponse

The ACL object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ACL**](ACL.md) |  | [optional] 

## Example

```python
from dns_config.models.create_acl_response import CreateACLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateACLResponse from a JSON string
create_acl_response_instance = CreateACLResponse.from_json(json)
# print the JSON string representation of the object
print(CreateACLResponse.to_json())

# convert the object into a dict
create_acl_response_dict = create_acl_response_instance.to_dict()
# create an instance of CreateACLResponse from a dict
create_acl_response_from_dict = CreateACLResponse.from_dict(create_acl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


