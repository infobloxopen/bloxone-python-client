# OspfConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **str** | OSPF area identifier; usually in the format of an IPv4 address (although not an address itself) | [optional] 
**area_type** | **str** |  | [optional] 
**authentication_key** | **str** |  | [optional] 
**authentication_key_id** | **int** |  | [optional] 
**authentication_type** | **str** |  | [optional] 
**cost** | **int** |  | [optional] 
**dead_interval** | **int** |  | [optional] 
**hello_interval** | **int** |  | [optional] 
**interface** | **str** | Name of the interface that is configured with external IP address of the host | [optional] 
**preamble** | **str** | Any predefined OSPF configuration, with embedded new lines; the preamble will be prepended to the generated BGP configuration. | [optional] 
**retransmit_interval** | **int** |  | [optional] 
**transmit_delay** | **int** |  | [optional] 

## Example

```python
from anycast.models.ospf_config import OspfConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OspfConfig from a JSON string
ospf_config_instance = OspfConfig.from_json(json)
# print the JSON string representation of the object
print(OspfConfig.to_json())

# convert the object into a dict
ospf_config_dict = ospf_config_instance.to_dict()
# create an instance of OspfConfig from a dict
ospf_config_from_dict = OspfConfig.from_dict(ospf_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


