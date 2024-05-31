# InheritedDtcConfig

Inheritance configuration for a field of type _DTCConfig_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_ttl** | [**Inheritance2InheritedUInt32**](Inheritance2InheritedUInt32.md) | Optional. Field config for _default_ttl_ field from _DTCConfig_ object. | [optional] 

## Example

```python
from dns_config.models.inherited_dtc_config import InheritedDtcConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedDtcConfig from a JSON string
inherited_dtc_config_instance = InheritedDtcConfig.from_json(json)
# print the JSON string representation of the object
print(InheritedDtcConfig.to_json())

# convert the object into a dict
inherited_dtc_config_dict = inherited_dtc_config_instance.to_dict()
# create an instance of InheritedDtcConfig from a dict
inherited_dtc_config_from_dict = InheritedDtcConfig.from_dict(inherited_dtc_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


