# CredentialPreference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_identifier_type** | **str** |  | [optional] 
**credential_type** | **str** |  | [optional] 

## Example

```python
from cloud_discovery.models.credential_preference import CredentialPreference

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialPreference from a JSON string
credential_preference_instance = CredentialPreference.from_json(json)
# print the JSON string representation of the object
print(CredentialPreference.to_json())

# convert the object into a dict
credential_preference_dict = credential_preference_instance.to_dict()
# create an instance of CredentialPreference from a dict
credential_preference_from_dict = CredentialPreference.from_dict(credential_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


