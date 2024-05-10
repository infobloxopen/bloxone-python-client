# DHCPUtilizationThreshold

A __DHCPUtilizationThreshold__ object represents threshold settings for DHCP utilization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether the DHCP utilization threshold is enabled or not. | 
**high** | **int** | The high threshold value for DHCP utilization in percentage. | 
**low** | **int** | The low threshold value for DHCP utilization in percentage. | 

## Example

```python
from ipam.models.dhcp_utilization_threshold import DHCPUtilizationThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPUtilizationThreshold from a JSON string
dhcp_utilization_threshold_instance = DHCPUtilizationThreshold.from_json(json)
# print the JSON string representation of the object
print(DHCPUtilizationThreshold.to_json())

# convert the object into a dict
dhcp_utilization_threshold_dict = dhcp_utilization_threshold_instance.to_dict()
# create an instance of DHCPUtilizationThreshold from a dict
dhcp_utilization_threshold_from_dict = DHCPUtilizationThreshold.from_dict(dhcp_utilization_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


