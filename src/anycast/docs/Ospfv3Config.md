# Ospfv3Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **str** | OSPF area identifier; usually in the format of an IPv4 address (although not an address itself) | [optional] 
**cost** | **int** |  | [optional] 
**dead_interval** | **int** |  | [optional] 
**hello_interval** | **int** |  | [optional] 
**interface** | **str** | Name of the interface that is configured with external IP address of the host | [optional] 
**retransmit_interval** | **int** |  | [optional] 
**transmit_delay** | **int** |  | [optional] 

## Example

```python
from anycast.models.ospfv3_config import Ospfv3Config

# TODO update the JSON string below
json = "{}"
# create an instance of Ospfv3Config from a JSON string
ospfv3_config_instance = Ospfv3Config.from_json(json)
# print the JSON string representation of the object
print(Ospfv3Config.to_json())

# convert the object into a dict
ospfv3_config_dict = ospfv3_config_instance.to_dict()
# create an instance of Ospfv3Config from a dict
ospfv3_config_from_dict = Ospfv3Config.from_dict(ospfv3_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


