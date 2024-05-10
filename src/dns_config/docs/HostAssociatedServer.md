# HostAssociatedServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | DNS server name. | [optional] [readonly] 

## Example

```python
from dns_config.models.host_associated_server import HostAssociatedServer

# TODO update the JSON string below
json = "{}"
# create an instance of HostAssociatedServer from a JSON string
host_associated_server_instance = HostAssociatedServer.from_json(json)
# print the JSON string representation of the object
print(HostAssociatedServer.to_json())

# convert the object into a dict
host_associated_server_dict = host_associated_server_instance.to_dict()
# create an instance of HostAssociatedServer from a dict
host_associated_server_from_dict = HostAssociatedServer.from_dict(host_associated_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


