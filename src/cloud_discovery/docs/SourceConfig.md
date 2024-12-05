# SourceConfig

Source configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_schedule_id** | **str** | Account Schedule ID. | [optional] [readonly] 
**accounts** | [**List[Account]**](Account.md) |  | [optional] 
**cloud_credential_id** | **str** | Cloud Credential ID. | [optional] 
**created_at** | **datetime** | Timestamp when the object has been created. | [optional] [readonly] 
**credential_config** | [**CredentialConfig**](CredentialConfig.md) | Credential configuration. Ex.: &#39;{    \&quot;access_identifier\&quot;: \&quot;arn:aws:iam::1234:role/access_for_discovery\&quot;,    \&quot;region\&quot;: \&quot;us-east-1\&quot;,    \&quot;enclave\&quot;: \&quot;commercial/gov\&quot;  }&#39;. | [optional] 
**deleted_at** | **datetime** | Timestamp when the object has been deleted. | [optional] [readonly] 
**id** | **str** | Auto-generated unique source config ID. Format BloxID. | [optional] [readonly] 
**restricted_to_accounts** | **List[str]** | Provider account IDs such as accountID/ SubscriptionID to be restricted for a given source_config. | [optional] 
**updated_at** | **datetime** | Timestamp when the object has been updated. | [optional] [readonly] 

## Example

```python
from cloud_discovery.models.source_config import SourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SourceConfig from a JSON string
source_config_instance = SourceConfig.from_json(json)
# print the JSON string representation of the object
print(SourceConfig.to_json())

# convert the object into a dict
source_config_dict = source_config_instance.to_dict()
# create an instance of SourceConfig from a dict
source_config_from_dict = SourceConfig.from_dict(source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


