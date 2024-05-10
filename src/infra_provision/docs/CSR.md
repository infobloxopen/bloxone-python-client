# CSR

Represents a certificate signing request from an on-prem host.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_code** | **str** |  | [optional] 
**client_ip** | [**TypesInetValue**](TypesInetValue.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**csr** | **bytearray** |  | [optional] 
**host_serial** | **str** |  | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**join_token** | [**JoinToken**](JoinToken.md) |  | [optional] 
**ophid** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 
**src_ip** | [**TypesInetValue**](TypesInetValue.md) |  | [optional] 
**state** | [**CSRState**](CSRState.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from infra_provision.models.csr import CSR

# TODO update the JSON string below
json = "{}"
# create an instance of CSR from a JSON string
csr_instance = CSR.from_json(json)
# print the JSON string representation of the object
print(CSR.to_json())

# convert the object into a dict
csr_dict = csr_instance.to_dict()
# create an instance of CSR from a dict
csr_from_dict = CSR.from_dict(csr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


