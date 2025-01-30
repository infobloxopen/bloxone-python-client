# Host

A DNS Host (_dns/host_) object associates DNS configuraton with hosts.   Automatically created and destroyed based on the hosts known to the platform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_name** | **str** | Host FQDN. | [optional] 
**address** | **str** | Host&#39;s primary IP Address. | [optional] [readonly] 
**anycast_addresses** | **List[str]** | Anycast address configured to the host. Order is not significant. | [optional] [readonly] 
**associated_server** | [**HostAssociatedServer**](HostAssociatedServer.md) | Host associated server configuration. | [optional] 
**comment** | **str** | Host description. | [optional] [readonly] 
**current_version** | **str** | Host current version. | [optional] [readonly] 
**dfp** | **bool** | Below _dfp_ field is deprecated and not supported anymore. The indication whether or not BloxOne DDI DNS and BloxOne TD DFP are both active on the host will be migrated into the new _dfp_service_ field. | [optional] [readonly] 
**dfp_service** | **str** | DFP service indicates whether or not BloxOne DDI DNS and BloxOne TD DFP are both active on the host. If so, BloxOne DDI DNS will augment recursive queries and forward them to BloxOne TD DFP. Allowed values:  * _unavailable_: BloxOne TD DFP application is not available,  * _enabled_: BloxOne TD DFP application is available and enabled,  * _disabled_: BloxOne TD DFP application is available but disabled. | [optional] [readonly] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**inheritance_sources** | [**HostInheritance**](HostInheritance.md) | Optional. Inheritance configuration. | [optional] 
**kerberos_keys** | [**List[KerberosKey]**](KerberosKey.md) | Optional. _kerberos_keys_ contains a list of keys for GSS-TSIG signed dynamic updates.  Defaults to empty. | [optional] 
**name** | **str** | Host display name. | [optional] [readonly] 
**ophid** | **str** | On-Prem Host ID. | [optional] [readonly] 
**protocol_absolute_name** | **str** | Host FQDN in punycode. | [optional] [readonly] 
**provider_id** | **str** | External provider identifier. | [optional] [readonly] 
**server** | **str** | The resource identifier. | [optional] 
**site_id** | **str** | Host site ID. | [optional] [readonly] 
**tags** | **object** | Host tagging specifics. | [optional] 
**type** | **str** | Defines the type of host. Allowed values:  * _bloxone_ddi_: host type is BloxOne DDI,  * _microsoft_azure_: host type is Microsoft Azure,  * _amazon_web_service_: host type is Amazon Web Services,  * _microsoft_active_directory_: host type is Microsoft Active Directory,  * _google_cloud_platform_: host type is Google Cloud Platform. | [optional] [readonly] 

## Example

```python
from dns_config.models.host import Host

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


