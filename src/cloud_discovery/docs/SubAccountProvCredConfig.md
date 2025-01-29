# SubAccountProvCredConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**role_arn** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from cloud_discovery.models.sub_account_prov_cred_config import SubAccountProvCredConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountProvCredConfig from a JSON string
sub_account_prov_cred_config_instance = SubAccountProvCredConfig.from_json(json)
# print the JSON string representation of the object
print(SubAccountProvCredConfig.to_json())

# convert the object into a dict
sub_account_prov_cred_config_dict = sub_account_prov_cred_config_instance.to_dict()
# create an instance of SubAccountProvCredConfig from a dict
sub_account_prov_cred_config_from_dict = SubAccountProvCredConfig.from_dict(sub_account_prov_cred_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


