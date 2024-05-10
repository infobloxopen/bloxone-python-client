# DHCPUtilization

The __DHCPUtilization__ object represents DHCP utilization statistics for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_free** | **str** | The total free IP addresses in the DHCP ranges in the scope of this object. It can be computed as _dhcp_total_ - _dhcp_used_. | [optional] [readonly] 
**dhcp_total** | **str** | The total IP addresses available in the DHCP ranges in the scope of this object. | [optional] [readonly] 
**dhcp_used** | **str** | The total IP addresses marked as used in the DHCP ranges in the scope of this object. | [optional] [readonly] 
**dhcp_utilization** | **int** | The percentage of used IP addresses relative to the total IP addresses available in the DHCP ranges in the scope of this object. | [optional] [readonly] 

## Example

```python
from ipam.models.dhcp_utilization import DHCPUtilization

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPUtilization from a JSON string
dhcp_utilization_instance = DHCPUtilization.from_json(json)
# print the JSON string representation of the object
print(DHCPUtilization.to_json())

# convert the object into a dict
dhcp_utilization_dict = dhcp_utilization_instance.to_dict()
# create an instance of DHCPUtilization from a dict
dhcp_utilization_from_dict = DHCPUtilization.from_dict(dhcp_utilization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


