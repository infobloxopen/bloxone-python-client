# Host

A DHCP __Host__ (_dhcp/host_) object associates a DHCP Config Profile with an on-prem host.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The primary IP address of the on-prem host. | [optional] [readonly] 
**anycast_addresses** | **List[str]** | Anycast address configured to the host. Order is not significant. | [optional] [readonly] 
**associated_server** | [**HostAssociatedServer**](HostAssociatedServer.md) |  | [optional] 
**comment** | **str** | The description for the on-prem host. | [optional] [readonly] 
**current_version** | **str** | Current dhcp application version of the host. | [optional] [readonly] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**ip_space** | **str** | The resource identifier. | [optional] 
**name** | **str** | The display name of the on-prem host. | [optional] [readonly] 
**ophid** | **str** | The on-prem host ID. | [optional] [readonly] 
**provider_id** | **str** | External provider identifier. | [optional] [readonly] 
**server** | **str** | The resource identifier. | [optional] 
**tags** | **object** | The tags of the on-prem host in JSON format. | [optional] 
**type** | **str** | Defines the type of host. Allowed values:  * _bloxone_ddi_: host type is BloxOne DDI,  * _microsoft_azure_: host type is Microsoft Azure,  * _amazon_web_service_: host type is Amazon Web Services.  * _microsoft_active_directory_: host type is Microsoft Active Directory. | [optional] [readonly] 

## Example

```python
from ipam.models.host import Host

# TODO update the JSON string below
json = "{}"
# create an instance of Host from a JSON string
host_instance = Host.from_json(json)
# print the JSON string representation of the object
print(Host.to_json())

# convert the object into a dict
host_dict = host_instance.to_dict()
# create an instance of Host from a dict
host_from_dict = Host.from_dict(host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


