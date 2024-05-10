# LeaseSubnet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource identifier. | [optional] [readonly] 

## Example

```python
from ipam.models.lease_subnet import LeaseSubnet

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseSubnet from a JSON string
lease_subnet_instance = LeaseSubnet.from_json(json)
# print the JSON string representation of the object
print(LeaseSubnet.to_json())

# convert the object into a dict
lease_subnet_dict = lease_subnet_instance.to_dict()
# create an instance of LeaseSubnet from a dict
lease_subnet_from_dict = LeaseSubnet.from_dict(lease_subnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


