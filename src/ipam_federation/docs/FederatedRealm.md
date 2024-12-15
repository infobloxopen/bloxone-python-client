# FederatedRealm

A __FederatedRealm__ object is a unique set of federated blocks per realm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_v4** | [**Allocation**](Allocation.md) | The aggregate of all Federated Blocks within the Realm. | [optional] 
**comment** | **str** | The description of the federated realm. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The name of the federated realm. May contain 1 to 256 characters; can include UTF-8. | 
**tags** | **object** | The tags for the federated realm in JSON format. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 

## Example

```python
from ipam_federation.models.federated_realm import FederatedRealm

# TODO update the JSON string below
json = "{}"
# create an instance of FederatedRealm from a JSON string
federated_realm_instance = FederatedRealm.from_json(json)
# print the JSON string representation of the object
print(FederatedRealm.to_json())

# convert the object into a dict
federated_realm_dict = federated_realm_instance.to_dict()
# create an instance of FederatedRealm from a dict
federated_realm_from_dict = FederatedRealm.from_dict(federated_realm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


