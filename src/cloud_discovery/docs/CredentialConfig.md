# CredentialConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_identifier** | **str** |  | [optional] 
**enclave** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from cloud_discovery.models.credential_config import CredentialConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialConfig from a JSON string
credential_config_instance = CredentialConfig.from_json(json)
# print the JSON string representation of the object
print(CredentialConfig.to_json())

# convert the object into a dict
credential_config_dict = credential_config_instance.to_dict()
# create an instance of CredentialConfig from a dict
credential_config_from_dict = CredentialConfig.from_dict(credential_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


