# DNSConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consolidated_zone_data_enabled** | **bool** |  | [optional] 
**split_view_enabled** | **bool** | split_view_enabled consolidates private zones into a single view, which is separate from the public zone view. | [optional] 
**sync_type** | **str** |  | [optional] 
**view_id** | **str** |  | [optional] 
**view_name** | **str** |  | [optional] 

## Example

```python
from cloud_discovery.models.dns_config import DNSConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DNSConfig from a JSON string
dns_config_instance = DNSConfig.from_json(json)
# print the JSON string representation of the object
print(DNSConfig.to_json())

# convert the object into a dict
dns_config_dict = dns_config_instance.to_dict()
# create an instance of DNSConfig from a dict
dns_config_from_dict = DNSConfig.from_dict(dns_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


