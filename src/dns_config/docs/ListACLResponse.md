# ListACLResponse

The ACL object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ACL]**](ACL.md) | List of ACL objects. | [optional] 

## Example

```python
from dns_config.models.list_acl_response import ListACLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListACLResponse from a JSON string
list_acl_response_instance = ListACLResponse.from_json(json)
# print the JSON string representation of the object
print(ListACLResponse.to_json())

# convert the object into a dict
list_acl_response_dict = list_acl_response_instance.to_dict()
# create an instance of ListACLResponse from a dict
list_acl_response_from_dict = ListACLResponse.from_dict(list_acl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


