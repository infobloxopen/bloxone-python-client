# SubAccountListResponseV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**ApiPageInfo**](ApiPageInfo.md) |  | [optional] 
**results** | [**List[SubAccountV2]**](SubAccountV2.md) |  | [optional] 

## Example

```python
from cloud_discovery.models.sub_account_list_response_v2 import SubAccountListResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountListResponseV2 from a JSON string
sub_account_list_response_v2_instance = SubAccountListResponseV2.from_json(json)
# print the JSON string representation of the object
print(SubAccountListResponseV2.to_json())

# convert the object into a dict
sub_account_list_response_v2_dict = sub_account_list_response_v2_instance.to_dict()
# create an instance of SubAccountListResponseV2 from a dict
sub_account_list_response_v2_from_dict = SubAccountListResponseV2.from_dict(sub_account_list_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


