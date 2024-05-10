# ServiceHostConfig

ServiceHostConfig is the specific configuration for each Service deployed on a Host

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_version** | **str** | The current version of the Service deployed on the Host. | [optional] 
**extra_data** | **str** | The field to carry any extra data specific to this configuration. | [optional] 
**host_id** | **str** | The resource identifier. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**service_id** | **str** | The resource identifier. | [optional] 
**service_type** | **str** | The type of the Service deployed on the Host (&#x60;dns&#x60;, &#x60;cdc&#x60;, etc.). | [optional] 
**upgraded_at** | **datetime** | The timestamp of the latest upgrade of the Host-specific Service configuration. | [optional] 

## Example

```python
from infra_mgmt.models.service_host_config import ServiceHostConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceHostConfig from a JSON string
service_host_config_instance = ServiceHostConfig.from_json(json)
# print the JSON string representation of the object
print(ServiceHostConfig.to_json())

# convert the object into a dict
service_host_config_dict = service_host_config_instance.to_dict()
# create an instance of ServiceHostConfig from a dict
service_host_config_from_dict = ServiceHostConfig.from_dict(service_host_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


