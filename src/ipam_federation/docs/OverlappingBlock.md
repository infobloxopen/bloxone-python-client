# OverlappingBlock

An __OverlappingBlock__ object (_federation/overlapping_block_) is a set of contiguous IP addresses with no gap, expressed as a CIDR block. It is explicitly associated with a Federated Realm, and implicitly with a Federated Block Parent. An __OverlappingBlock__ in a given realm is said to be the child of the closest enclosing parent. An __OverlappingBlock__ indicates an address range that may be managed independently by all participating IPAM services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address field in form “a.b.c.d/n” where the “/n” may be omitted. In this case, the CIDR value must be defined in the _cidr_ field. When reading, the _address_ field is always in the form “a.b.c.d”. | 
**cidr** | **int** | The CIDR of the overlapping block. This is required, if _address_ does not specify it in its input. | [optional] 
**comment** | **str** | The description for the overlapping block. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**federated_realm** | **str** | The resource identifier. | 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The name of the overlapping block. May contain 1 to 256 characters. Can include UTF-8. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**protocol** | **str** | The type of protocol of overlapping block (_ip4_ or _ip6_). | [optional] [readonly] 
**tags** | **object** | The tags for the overlapping block in JSON format. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 

## Example

```python
from ipam_federation.models.overlapping_block import OverlappingBlock

# TODO update the JSON string below
json = "{}"
# create an instance of OverlappingBlock from a JSON string
overlapping_block_instance = OverlappingBlock.from_json(json)
# print the JSON string representation of the object
print(OverlappingBlock.to_json())

# convert the object into a dict
overlapping_block_dict = overlapping_block_instance.to_dict()
# create an instance of OverlappingBlock from a dict
overlapping_block_from_dict = OverlappingBlock.from_dict(overlapping_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


