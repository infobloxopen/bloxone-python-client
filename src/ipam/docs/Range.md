# Range

A __Range__ object (_ipam/range_) represents a set of contiguous IP addresses in the same IP space with no gap, expressed as a (start, end) pair within a given subnet that are grouped together for administrative purpose and protocol management. The start and end values are not required to align with CIDR boundaries. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The description for the range. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**dhcp_host** | **str** | The resource identifier. | [optional] 
**dhcp_options** | [**List[OptionItem]**](OptionItem.md) | The list of DHCP options. May be either a specific option or a group of options. | [optional] 
**disable_dhcp** | **bool** | Optional. _true_ to disable object. A disabled object is effectively non-existent when generating configuration.  Defaults to _false_. | [optional] 
**end** | **str** | The end IP address of the range. | 
**exclusion_ranges** | [**List[ExclusionRange]**](ExclusionRange.md) | The list of all exclusion ranges in the scope of the range. | [optional] 
**filters** | [**List[AccessFilter]**](AccessFilter.md) | The list of all allow/deny filters of the range. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**inheritance_assigned_hosts** | [**List[InheritanceAssignedHost]**](InheritanceAssignedHost.md) | The list of the inheritance assigned hosts of the object. | [optional] [readonly] 
**inheritance_parent** | **str** | The resource identifier. | [optional] 
**inheritance_sources** | [**DHCPOptionsInheritance**](DHCPOptionsInheritance.md) | The DHCP inheritance configuration for the range. | [optional] 
**name** | **str** | The name of the range. May contain 1 to 256 characters. Can include UTF-8. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**protocol** | **str** | The type of protocol (_ip4_ or _ip6_). | [optional] [readonly] 
**space** | **str** | The resource identifier. | [optional] 
**start** | **str** | The start IP address of the range. | 
**tags** | **object** | The tags for the range in JSON format. | [optional] 
**threshold** | [**UtilizationThreshold**](UtilizationThreshold.md) | The utilization threshold settings for the range. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 
**utilization** | [**Utilization**](Utilization.md) | The utilization statistics of IPV4 addresses for the range. | [optional] [readonly] 
**utilization_v6** | [**UtilizationV6**](UtilizationV6.md) | The utilization of IPV6 addresses in the range. | [optional] [readonly] 

## Example

```python
from ipam.models.range import Range

# TODO update the JSON string below
json = "{}"
# create an instance of Range from a JSON string
range_instance = Range.from_json(json)
# print the JSON string representation of the object
print(Range.to_json())

# convert the object into a dict
range_dict = range_instance.to_dict()
# create an instance of Range from a dict
range_from_dict = Range.from_dict(range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


