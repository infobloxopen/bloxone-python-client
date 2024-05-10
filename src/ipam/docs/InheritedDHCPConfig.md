# InheritedDHCPConfig

The inheritance configuration for a field of type _DHCPConfig_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandoned_reclaim_time** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) |  | [optional] 
**abandoned_reclaim_time_v6** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) |  | [optional] 
**allow_unknown** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) |  | [optional] 
**allow_unknown_v6** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) |  | [optional] 
**echo_client_id** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) |  | [optional] 
**filters** | [**InheritedDHCPConfigFilterList**](InheritedDHCPConfigFilterList.md) |  | [optional] 
**filters_v6** | [**InheritedDHCPConfigFilterList**](InheritedDHCPConfigFilterList.md) |  | [optional] 
**ignore_client_uid** | [**InheritanceInheritedBool**](InheritanceInheritedBool.md) |  | [optional] 
**ignore_list** | [**InheritedDHCPConfigIgnoreItemList**](InheritedDHCPConfigIgnoreItemList.md) |  | [optional] 
**lease_time** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) |  | [optional] 
**lease_time_v6** | [**InheritanceInheritedUInt32**](InheritanceInheritedUInt32.md) |  | [optional] 

## Example

```python
from ipam.models.inherited_dhcp_config import InheritedDHCPConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedDHCPConfig from a JSON string
inherited_dhcp_config_instance = InheritedDHCPConfig.from_json(json)
# print the JSON string representation of the object
print(InheritedDHCPConfig.to_json())

# convert the object into a dict
inherited_dhcp_config_dict = inherited_dhcp_config_instance.to_dict()
# create an instance of InheritedDHCPConfig from a dict
inherited_dhcp_config_from_dict = InheritedDHCPConfig.from_dict(inherited_dhcp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


