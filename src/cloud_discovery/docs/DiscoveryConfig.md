# DiscoveryConfig

Discovery configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_preference** | **str** | Account preference. For ex.: single, multiple, auto-discover-multiple. | 
**additional_config** | [**AdditionalConfig**](AdditionalConfig.md) | Additional configuration. Ex.: &#39;{    \&quot;excluded_object_types\&quot;: [],    \&quot;exclusion_account_list\&quot;: [],    \&quot;zone_forwarding\&quot;: \&quot;true\&quot; or \&quot;false\&quot; }&#39;. | [optional] 
**created_at** | **datetime** | Timestamp when the object has been created. | [optional] [readonly] 
**credential_preference** | [**CredentialPreference**](CredentialPreference.md) | Credential preference. Ex.: &#39;{    \&quot;type\&quot;: \&quot;static\&quot; or \&quot;delegated\&quot;,    \&quot;access_identifier_type\&quot;: \&quot;role_arn\&quot; or \&quot;tenant_id\&quot; or \&quot;project_id\&quot;  }&#39;. | [optional] 
**deleted_at** | **datetime** | Timestamp when the object has been deleted. | [optional] [readonly] 
**description** | **str** | Description of the discovery config. Optional. | [optional] 
**desired_state** | **str** | Desired state. Default is \&quot;enabled\&quot;. | [optional] 
**destination_types_enabled** | **List[str]** | Destinations types enabled: Ex.: DNS, IPAM and ACCOUNT. | [optional] 
**destinations** | [**List[Destination]**](Destination.md) | Destinations. | [optional] 
**id** | **str** | Auto-generated unique discovery config ID. Format BloxID. | [optional] [readonly] 
**last_sync** | **datetime** | Last sync timestamp. | [optional] [readonly] 
**name** | **str** | Name of the discovery config. | 
**provider_type** | **str** | Provider type. Ex.: Amazon Web Services, Google Cloud Platform, Microsoft Azure. | 
**source_configs** | [**List[SourceConfig]**](SourceConfig.md) | Source configs. | [optional] 
**status** | **str** | Status of the sync operation. In single account case, Its the combined status of account &amp; all the destinations statuses In auto discover case, Its the status of the account discovery only. | [optional] [readonly] 
**status_message** | **str** | Aggregate status message of the sync operation. | [optional] [readonly] 
**sync_interval** | **str** |  | [optional] 
**tags** | **object** | Tagging specifics. | [optional] 
**updated_at** | **datetime** | Timestamp when the object has been updated. | [optional] [readonly] 

## Example

```python
from cloud_discovery.models.discovery_config import DiscoveryConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryConfig from a JSON string
discovery_config_instance = DiscoveryConfig.from_json(json)
# print the JSON string representation of the object
print(DiscoveryConfig.to_json())

# convert the object into a dict
discovery_config_dict = discovery_config_instance.to_dict()
# create an instance of DiscoveryConfig from a dict
discovery_config_from_dict = DiscoveryConfig.from_dict(discovery_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


