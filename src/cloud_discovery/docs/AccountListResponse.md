# AccountListResponse

The Account object List response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**ApiPageInfo**](ApiPageInfo.md) |  | [optional] 
**results** | [**List[Account]**](Account.md) |  | [optional] 

## Example

```python
from cloud_discovery.models.account_list_response import AccountListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountListResponse from a JSON string
account_list_response_instance = AccountListResponse.from_json(json)
# print the JSON string representation of the object
print(AccountListResponse.to_json())

# convert the object into a dict
account_list_response_dict = account_list_response_instance.to_dict()
# create an instance of AccountListResponse from a dict
account_list_response_from_dict = AccountListResponse.from_dict(account_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


