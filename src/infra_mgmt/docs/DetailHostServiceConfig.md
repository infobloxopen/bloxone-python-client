# DetailHostServiceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_version** | **str** | The current version of the Service deployed on the Host. | [optional] 
**service_id** | **str** | The resource identifier. | [optional] 
**service_name** | **str** | The name of the Service. | [optional] 
**service_type** | **str** | The type of the Service deployed on the Host (&#x60;dns&#x60;, &#x60;cdc&#x60;, etc.). | [optional] 
**status** | [**ShortServiceStatus**](ShortServiceStatus.md) |  | [optional] 
**upgraded_at** | **datetime** | The timestamp of the latest upgrade of the Host-specific Service configuration. | [optional] 

## Example

```python
from infra_mgmt.models.detail_host_service_config import DetailHostServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DetailHostServiceConfig from a JSON string
detail_host_service_config_instance = DetailHostServiceConfig.from_json(json)
# print the JSON string representation of the object
print(DetailHostServiceConfig.to_json())

# convert the object into a dict
detail_host_service_config_dict = detail_host_service_config_instance.to_dict()
# create an instance of DetailHostServiceConfig from a dict
detail_host_service_config_from_dict = DetailHostServiceConfig.from_dict(detail_host_service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


