# ProviderReadResponse

The Provider object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**DiscoveryConfig**](DiscoveryConfig.md) |  | [optional] 

## Example

```python
from cloud_discovery.models.provider_read_response import ProviderReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderReadResponse from a JSON string
provider_read_response_instance = ProviderReadResponse.from_json(json)
# print the JSON string representation of the object
print(ProviderReadResponse.to_json())

# convert the object into a dict
provider_read_response_dict = provider_read_response_instance.to_dict()
# create an instance of ProviderReadResponse from a dict
provider_read_response_from_dict = ProviderReadResponse.from_dict(provider_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


