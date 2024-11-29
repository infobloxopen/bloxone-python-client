# ReservedBlock

A __ReservedBlock__ object (_federation/reserved_block_) is a set of contiguous IP addresses with no gap, expressed as a CIDR block. It is explicitly associated with a Federated Realm. A __ReservedBlock__ indicates an address range for which authority is expressly forbidden. Cooperating IPAM services must not make allocations in this range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address field in form “a.b.c.d/n” where the “/n” may be omitted. In this case, the CIDR value must be defined in the _cidr_ field. When reading, the _address_ field is always in the form “a.b.c.d”. | 
**cidr** | **int** | The CIDR of the reserved block. This is required field, if _address_ does not specify it in its input. | [optional] 
**comment** | **str** | The description for the reserved block. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**federated_realm** | **str** | The resource identifier. | 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The name of the reserved block. May contain 1 to 256 characters. Can include UTF-8. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**protocol** | **str** | The type of protocol of reserved block (_ip4_ or _ip6_). | [optional] [readonly] 
**tags** | **object** | The tags for the reserved block in JSON format. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 

## Example

```python
from ipam_federation.models.reserved_block import ReservedBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ReservedBlock from a JSON string
reserved_block_instance = ReservedBlock.from_json(json)
# print the JSON string representation of the object
print(ReservedBlock.to_json())

# convert the object into a dict
reserved_block_dict = reserved_block_instance.to_dict()
# create an instance of ReservedBlock from a dict
reserved_block_from_dict = ReservedBlock.from_dict(reserved_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


