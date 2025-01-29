# AdditionalConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_accounts** | **List[str]** |  | [optional] 
**forward_zone_enabled** | **bool** |  | [optional] 
**internal_ranges_enabled** | **bool** |  | [optional] 
**object_type** | [**ObjectType**](ObjectType.md) |  | [optional] 

## Example

```python
from cloud_discovery.models.additional_config import AdditionalConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalConfig from a JSON string
additional_config_instance = AdditionalConfig.from_json(json)
# print the JSON string representation of the object
print(AdditionalConfig.to_json())

# convert the object into a dict
additional_config_dict = additional_config_instance.to_dict()
# create an instance of AdditionalConfig from a dict
additional_config_from_dict = AdditionalConfig.from_dict(additional_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


