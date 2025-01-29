# ProviderListResponse

The Provider object List response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**ApiPageInfo**](ApiPageInfo.md) |  | [optional] 
**results** | [**List[DiscoveryConfig]**](DiscoveryConfig.md) |  | [optional] 

## Example

```python
from cloud_discovery.models.provider_list_response import ProviderListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderListResponse from a JSON string
provider_list_response_instance = ProviderListResponse.from_json(json)
# print the JSON string representation of the object
print(ProviderListResponse.to_json())

# convert the object into a dict
provider_list_response_dict = provider_list_response_instance.to_dict()
# create an instance of ProviderListResponse from a dict
provider_list_response_from_dict = ProviderListResponse.from_dict(provider_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


