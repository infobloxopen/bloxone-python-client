# CreateFederatedRealmResponse

The response format to create the __FederatedRealm__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**FederatedRealm**](FederatedRealm.md) | The created Federated Realm object. | [optional] 

## Example

```python
from ipam_federation.models.create_federated_realm_response import CreateFederatedRealmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFederatedRealmResponse from a JSON string
create_federated_realm_response_instance = CreateFederatedRealmResponse.from_json(json)
# print the JSON string representation of the object
print(CreateFederatedRealmResponse.to_json())

# convert the object into a dict
create_federated_realm_response_dict = create_federated_realm_response_instance.to_dict()
# create an instance of CreateFederatedRealmResponse from a dict
create_federated_realm_response_from_dict = CreateFederatedRealmResponse.from_dict(create_federated_realm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


