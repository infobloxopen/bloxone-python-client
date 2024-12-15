# SubAccountListRequestV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** |  | [optional] 
**credential_id** | **str** |  | [optional] 
**fields** | **str** | atlas.api.field_selection | [optional] 
**provider_credentials_config** | [**SubAccountProvCredConfig**](SubAccountProvCredConfig.md) |  | [optional] 
**provider_type** | **str** |  | [optional] 

## Example

```python
from cloud_discovery.models.sub_account_list_request_v2 import SubAccountListRequestV2

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountListRequestV2 from a JSON string
sub_account_list_request_v2_instance = SubAccountListRequestV2.from_json(json)
# print the JSON string representation of the object
print(SubAccountListRequestV2.to_json())

# convert the object into a dict
sub_account_list_request_v2_dict = sub_account_list_request_v2_instance.to_dict()
# create an instance of SubAccountListRequestV2 from a dict
sub_account_list_request_v2_from_dict = SubAccountListRequestV2.from_dict(sub_account_list_request_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


