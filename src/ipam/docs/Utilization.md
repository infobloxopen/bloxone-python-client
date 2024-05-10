# Utilization

The __Utilization__ object represents IP address usage statistics for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandon_utilization** | **int** | The percentage of abandoned IP addresses relative to the total IP addresses available in the scope of the object. | [optional] [readonly] 
**abandoned** | **str** | The number of IP addresses in the scope of the object which are in the abandoned state (issued by a DHCP server and then declined by the client). | [optional] [readonly] 
**dynamic** | **str** | The number of IP addresses handed out by DHCP in the scope of the object. This includes all leased addresses, fixed addresses that are defined but not currently leased and abandoned leases. | [optional] [readonly] 
**free** | **str** | The number of IP addresses available in the scope of the object. | [optional] [readonly] 
**static** | **str** | The number of defined IP addresses such as reservations or DNS records. It can be computed as _static_ &#x3D; _used_ - _dynamic_. | [optional] [readonly] 
**total** | **str** | The total number of IP addresses available in the scope of the object. | [optional] [readonly] 
**used** | **str** | The number of IP addresses used in the scope of the object. | [optional] [readonly] 
**utilization** | **int** | The percentage of used IP addresses relative to the total IP addresses available in the scope of the object. | [optional] [readonly] 

## Example

```python
from ipam.models.utilization import Utilization

# TODO update the JSON string below
json = "{}"
# create an instance of Utilization from a JSON string
utilization_instance = Utilization.from_json(json)
# print the JSON string representation of the object
print(Utilization.to_json())

# convert the object into a dict
utilization_dict = utilization_instance.to_dict()
# create an instance of Utilization from a dict
utilization_from_dict = Utilization.from_dict(utilization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


