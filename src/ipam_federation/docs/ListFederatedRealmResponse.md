# ListFederatedRealmResponse

The response format to retrieve __FederatedRealm__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[FederatedRealm]**](FederatedRealm.md) | The list of FederatedRealm objects. | [optional] 

## Example

```python
from ipam_federation.models.list_federated_realm_response import ListFederatedRealmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListFederatedRealmResponse from a JSON string
list_federated_realm_response_instance = ListFederatedRealmResponse.from_json(json)
# print the JSON string representation of the object
print(ListFederatedRealmResponse.to_json())

# convert the object into a dict
list_federated_realm_response_dict = list_federated_realm_response_instance.to_dict()
# create an instance of ListFederatedRealmResponse from a dict
list_federated_realm_response_from_dict = ListFederatedRealmResponse.from_dict(list_federated_realm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


