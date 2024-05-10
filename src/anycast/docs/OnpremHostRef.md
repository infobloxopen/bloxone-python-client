# OnpremHostRef

Struct on-prem host reference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**ip_address** | **str** | IPv4 address of the host in string format | [optional] 
**ipv6_address** | **str** | IPv6 address of the host in string format | [optional] 
**name** | **str** |  | [optional] 
**ophid** | **str** | Unique 32-character string identifier assigned to the host | [optional] [readonly] 
**runtime_status** | **str** |  | [optional] 

## Example

```python
from anycast.models.onprem_host_ref import OnpremHostRef

# TODO update the JSON string below
json = "{}"
# create an instance of OnpremHostRef from a JSON string
onprem_host_ref_instance = OnpremHostRef.from_json(json)
# print the JSON string representation of the object
print(OnpremHostRef.to_json())

# convert the object into a dict
onprem_host_ref_dict = onprem_host_ref_instance.to_dict()
# create an instance of OnpremHostRef from a dict
onprem_host_ref_from_dict = OnpremHostRef.from_dict(onprem_host_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


