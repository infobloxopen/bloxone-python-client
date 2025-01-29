# ReadFederatedRealmResponse

The response format to retrieve the __FederatedRealm__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**FederatedRealm**](FederatedRealm.md) | The FederatedRealm object. | [optional] 

## Example

```python
from ipam_federation.models.read_federated_realm_response import ReadFederatedRealmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadFederatedRealmResponse from a JSON string
read_federated_realm_response_instance = ReadFederatedRealmResponse.from_json(json)
# print the JSON string representation of the object
print(ReadFederatedRealmResponse.to_json())

# convert the object into a dict
read_federated_realm_response_dict = read_federated_realm_response_instance.to_dict()
# create an instance of ReadFederatedRealmResponse from a dict
read_federated_realm_response_from_dict = ReadFederatedRealmResponse.from_dict(read_federated_realm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


