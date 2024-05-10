# ACL

Named ACL (Access Control List).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for ACL. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**list** | [**List[ACLItem]**](ACLItem.md) | Optional. Ordered list of access control elements.  Elements are evaluated in order to determine access. If evaluation reaches the end of the list then access is denied. | [optional] 
**name** | **str** | ACL object name. | 
**tags** | **object** | Tagging specifics. | [optional] 

## Example

```python
from dns_config.models.acl import ACL

# TODO update the JSON string below
json = "{}"
# create an instance of ACL from a JSON string
acl_instance = ACL.from_json(json)
# print the JSON string representation of the object
print(ACL.to_json())

# convert the object into a dict
acl_dict = acl_instance.to_dict()
# create an instance of ACL from a dict
acl_from_dict = ACL.from_dict(acl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


