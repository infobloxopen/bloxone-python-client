# DTCConfig

Construct for fields: _default_ttl_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_ttl** | **int** | Optional. Default TTL for synthesized DTC records (value in seconds).  Defaults to 300. | [optional] 

## Example

```python
from dns_config.models.dtc_config import DTCConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DTCConfig from a JSON string
dtc_config_instance = DTCConfig.from_json(json)
# print the JSON string representation of the object
print(DTCConfig.to_json())

# convert the object into a dict
dtc_config_dict = dtc_config_instance.to_dict()
# create an instance of DTCConfig from a dict
dtc_config_from_dict = DTCConfig.from_dict(dtc_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


