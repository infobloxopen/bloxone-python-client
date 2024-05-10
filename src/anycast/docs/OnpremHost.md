# OnpremHost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anycast_config_refs** | [**List[AnycastConfigRef]**](AnycastConfigRef.md) |  | [optional] 
**config_bgp** | [**BgpConfig**](BgpConfig.md) |  | [optional] 
**config_ospf** | [**OspfConfig**](OspfConfig.md) |  | [optional] 
**config_ospfv3** | [**Ospfv3Config**](Ospfv3Config.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] [readonly] 
**ip_address** | **str** | IPv4 address of the on-prem host | [optional] 
**ipv6_address** | **str** | IPv6 address of the on-prem host | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from anycast.models.onprem_host import OnpremHost

# TODO update the JSON string below
json = "{}"
# create an instance of OnpremHost from a JSON string
onprem_host_instance = OnpremHost.from_json(json)
# print the JSON string representation of the object
print(OnpremHost.to_json())

# convert the object into a dict
onprem_host_dict = onprem_host_instance.to_dict()
# create an instance of OnpremHost from a dict
onprem_host_from_dict = OnpremHost.from_dict(onprem_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


