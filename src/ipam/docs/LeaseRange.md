# LeaseRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource identifier. | [optional] [readonly] 

## Example

```python
from ipam.models.lease_range import LeaseRange

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseRange from a JSON string
lease_range_instance = LeaseRange.from_json(json)
# print the JSON string representation of the object
print(LeaseRange.to_json())

# convert the object into a dict
lease_range_dict = lease_range_instance.to_dict()
# create an instance of LeaseRange from a dict
lease_range_from_dict = LeaseRange.from_dict(lease_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


