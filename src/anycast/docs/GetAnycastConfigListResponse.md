# GetAnycastConfigListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AnycastConfig]**](AnycastConfig.md) |  | [optional] 

## Example

```python
from anycast.models.get_anycast_config_list_response import GetAnycastConfigListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnycastConfigListResponse from a JSON string
get_anycast_config_list_response_instance = GetAnycastConfigListResponse.from_json(json)
# print the JSON string representation of the object
print(GetAnycastConfigListResponse.to_json())

# convert the object into a dict
get_anycast_config_list_response_dict = get_anycast_config_list_response_instance.to_dict()
# create an instance of GetAnycastConfigListResponse from a dict
get_anycast_config_list_response_from_dict = GetAnycastConfigListResponse.from_dict(get_anycast_config_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


