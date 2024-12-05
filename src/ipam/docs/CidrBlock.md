# CidrBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address part of the CidrBlock. | [optional] [readonly] 
**cidr** | **int** | The CIDR part of the CidrBlock. | [optional] [readonly] 
**federated_realms** | **List[str]** | Reserved for future use. | [optional] [readonly] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**parent** | **str** | The resource identifier. | [optional] 
**space** | **str** | The resource identifier. | [optional] 

## Example

```python
from ipam.models.cidr_block import CidrBlock

# TODO update the JSON string below
json = "{}"
# create an instance of CidrBlock from a JSON string
cidr_block_instance = CidrBlock.from_json(json)
# print the JSON string representation of the object
print(CidrBlock.to_json())

# convert the object into a dict
cidr_block_dict = cidr_block_instance.to_dict()
# create an instance of CidrBlock from a dict
cidr_block_from_dict = CidrBlock.from_dict(cidr_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


