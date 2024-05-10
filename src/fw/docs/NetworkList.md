# NetworkList

The Network List object.  Before you can apply security policies, you must first define the networks that you want to protect from malicious attacks. The first step in configuring BloxOne Cloud is to set up DNS Firewall by defining your remote networks. You identify these external networks by their IP addresses. A network can contain a group of IPv4 or IPv6 addresses or blocks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **datetime** | The time when this Network List object was created. | [optional] [readonly] 
**description** | **str** | The brief description for the network list. | [optional] 
**id** | **int** | The Network List object identifier. | [optional] [readonly] 
**items** | **List[str]** | The list of networks&#39; CIDRs that are subject for malicious attacks protection. | [optional] 
**name** | **str** | The name of the network list. | [optional] 
**policy_id** | **int** | The identifier of the security policy with which the network list is associated. | [optional] [readonly] 
**updated_time** | **datetime** | The time when this Network List object was last updated. | [optional] [readonly] 

## Example

```python
from fw.models.network_list import NetworkList

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkList from a JSON string
network_list_instance = NetworkList.from_json(json)
# print the JSON string representation of the object
print(NetworkList.to_json())

# convert the object into a dict
network_list_dict = network_list_instance.to_dict()
# create an instance of NetworkList from a dict
network_list_from_dict = NetworkList.from_dict(network_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


