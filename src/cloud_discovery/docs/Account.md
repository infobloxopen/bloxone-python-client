# Account

Source account information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**composite_status** | **str** |  | [optional] 
**composite_status_message** | **str** | Status message of the sync operation. | [optional] 
**created_at** | **datetime** | Timestamp when the object has been created. | [optional] [readonly] 
**deleted_at** | **datetime** | Timestamp when the object has been deleted. | [optional] [readonly] 
**dhcp_server_id** | **str** |  | [optional] [readonly] 
**dns_server_id** | **str** | DNS Server ID. | [optional] [readonly] 
**id** | **str** | Auto-generated unique source account ID. Format BloxID. | [optional] [readonly] 
**last_successful_sync** | **datetime** | Last successful sync timestamp. | [optional] [readonly] 
**last_sync** | **datetime** | Last sync timestamp. | [optional] [readonly] 
**name** | **str** | Name of the source account. | 
**parent_id** | **str** | Parent ID. | [optional] 
**percent_complete** | **int** | Sync progress as a percentage. | [optional] [readonly] 
**provider_account_id** | **str** |  | [optional] 
**schedule_id** | **str** | Schedule ID. | [optional] [readonly] 
**state** | **str** |  | [optional] [readonly] 
**status** | **str** | Status of the sync operation. | [optional] [readonly] 
**status_message** | **str** | Status message of the sync operation. | [optional] [readonly] 
**updated_at** | **datetime** | Timestamp when the object has been updated. | [optional] [readonly] 

## Example

```python
from cloud_discovery.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


