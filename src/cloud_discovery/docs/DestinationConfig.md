# DestinationConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | [**DNSConfig**](DNSConfig.md) |  | [optional] 
**ipam** | [**IPAMConfig**](IPAMConfig.md) |  | [optional] 

## Example

```python
from cloud_discovery.models.destination_config import DestinationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationConfig from a JSON string
destination_config_instance = DestinationConfig.from_json(json)
# print the JSON string representation of the object
print(DestinationConfig.to_json())

# convert the object into a dict
destination_config_dict = destination_config_instance.to_dict()
# create an instance of DestinationConfig from a dict
destination_config_from_dict = DestinationConfig.from_dict(destination_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


