# AnycastConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**AnycastConfig**](AnycastConfig.md) |  | [optional] 

## Example

```python
from anycast.models.anycast_config_response import AnycastConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnycastConfigResponse from a JSON string
anycast_config_response_instance = AnycastConfigResponse.from_json(json)
# print the JSON string representation of the object
print(AnycastConfigResponse.to_json())

# convert the object into a dict
anycast_config_response_dict = anycast_config_response_instance.to_dict()
# create an instance of AnycastConfigResponse from a dict
anycast_config_response_from_dict = AnycastConfigResponse.from_dict(anycast_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


