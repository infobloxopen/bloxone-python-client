# ACLItem

Element in an ACL.   Error if both _acl_ and _address_ are given.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** | Access permission for _element_.  Allowed values:  * _allow_,  * _deny_. | 
**acl** | **str** | The resource identifier. | [optional] 
**address** | **str** | Optional. Data for _ip_ _element_.  Must be empty if _element_ is not _ip_. | [optional] 
**element** | **str** | Type of element.  Allowed values:  * _any_,  * _ip_,  * _acl_,  * _tsig_key_. | 
**tsig_key** | [**TSIGKey**](TSIGKey.md) |  | [optional] 

## Example

```python
from dns_config.models.acl_item import ACLItem

# TODO update the JSON string below
json = "{}"
# create an instance of ACLItem from a JSON string
acl_item_instance = ACLItem.from_json(json)
# print the JSON string representation of the object
print(ACLItem.to_json())

# convert the object into a dict
acl_item_dict = acl_item_instance.to_dict()
# create an instance of ACLItem from a dict
acl_item_from_dict = ACLItem.from_dict(acl_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


