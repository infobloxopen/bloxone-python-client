# DHCPServiceInstance

A DHCP Service (_dhcp/service_) object associates DHCP configuration with the DHCP host services.   Automatically created and destroyed based on the hosts known to the platform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_hosts** | [**List[AssociatedHost]**](AssociatedHost.md) |  | [optional] 
**associated_server** | [**HostAssociatedServer**](HostAssociatedServer.md) |  | [optional] 
**comment** | **str** | The comment for the service. | [optional] [readonly] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**ip_space** | **str** | The resource identifier. | [optional] 
**name** | **str** | The display name of the service. | [optional] [readonly] 
**tags** | **object** | The tags of the service host in JSON format. | [optional] 

## Example

```python
from ipam.models.dhcp_service_instance import DHCPServiceInstance

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPServiceInstance from a JSON string
dhcp_service_instance_instance = DHCPServiceInstance.from_json(json)
# print the JSON string representation of the object
print(DHCPServiceInstance.to_json())

# convert the object into a dict
dhcp_service_instance_dict = dhcp_service_instance_instance.to_dict()
# create an instance of DHCPServiceInstance from a dict
dhcp_service_instance_from_dict = DHCPServiceInstance.from_dict(dhcp_service_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


