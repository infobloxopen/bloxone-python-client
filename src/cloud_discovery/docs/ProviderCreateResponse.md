# ProviderCreateResponse

The Provider object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**DiscoveryConfig**](DiscoveryConfig.md) |  | [optional] 

## Example

```python
from cloud_discovery.models.provider_create_response import ProviderCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderCreateResponse from a JSON string
provider_create_response_instance = ProviderCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ProviderCreateResponse.to_json())

# convert the object into a dict
provider_create_response_dict = provider_create_response_instance.to_dict()
# create an instance of ProviderCreateResponse from a dict
provider_create_response_from_dict = ProviderCreateResponse.from_dict(provider_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


