# Allocation

The __Allocation__ tracks the distribution of Federated Blocks within each of the supported objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | **int** | Percent of total space allocated. | [optional] [readonly] 
**delegated** | **int** | Percent of total space delegated. | [optional] [readonly] 
**overlapping** | **int** | Percent of total space in overlapping blocks. | [optional] [readonly] 
**reserved** | **int** | Percent of total space reserved. | [optional] [readonly] 

## Example

```python
from ipam_federation.models.allocation import Allocation

# TODO update the JSON string below
json = "{}"
# create an instance of Allocation from a JSON string
allocation_instance = Allocation.from_json(json)
# print the JSON string representation of the object
print(Allocation.to_json())

# convert the object into a dict
allocation_dict = allocation_instance.to_dict()
# create an instance of Allocation from a dict
allocation_from_dict = Allocation.from_dict(allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


