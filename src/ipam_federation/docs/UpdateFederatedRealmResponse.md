# UpdateFederatedRealmResponse

The response format to update the __FederatedRealm__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**FederatedRealm**](FederatedRealm.md) | The FederatedRealm object. | [optional] 

## Example

```python
from ipam_federation.models.update_federated_realm_response import UpdateFederatedRealmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFederatedRealmResponse from a JSON string
update_federated_realm_response_instance = UpdateFederatedRealmResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateFederatedRealmResponse.to_json())

# convert the object into a dict
update_federated_realm_response_dict = update_federated_realm_response_instance.to_dict()
# create an instance of UpdateFederatedRealmResponse from a dict
update_federated_realm_response_from_dict = UpdateFederatedRealmResponse.from_dict(update_federated_realm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


