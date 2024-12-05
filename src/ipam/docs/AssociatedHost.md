# AssociatedHost

A DHCP Host (_dhcp/host_) object associates DHCP configuraton with hosts.   Automatically created and destroyed based on the hosts known to the platform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The primary IP address of the on-prem host. | [optional] [readonly] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The DHCP host name. | [optional] [readonly] 
**ophid** | **str** | The on-prem host ID. | [optional] [readonly] 

## Example

```python
from ipam.models.associated_host import AssociatedHost

# TODO update the JSON string below
json = "{}"
# create an instance of AssociatedHost from a JSON string
associated_host_instance = AssociatedHost.from_json(json)
# print the JSON string representation of the object
print(AssociatedHost.to_json())

# convert the object into a dict
associated_host_dict = associated_host_instance.to_dict()
# create an instance of AssociatedHost from a dict
associated_host_from_dict = AssociatedHost.from_dict(associated_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


