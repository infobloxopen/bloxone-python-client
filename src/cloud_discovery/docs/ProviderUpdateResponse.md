# ProviderUpdateResponse

The Provider object to update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**DiscoveryConfig**](DiscoveryConfig.md) |  | [optional] 

## Example

```python
from cloud_discovery.models.provider_update_response import ProviderUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderUpdateResponse from a JSON string
provider_update_response_instance = ProviderUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(ProviderUpdateResponse.to_json())

# convert the object into a dict
provider_update_response_dict = provider_update_response_instance.to_dict()
# create an instance of ProviderUpdateResponse from a dict
provider_update_response_from_dict = ProviderUpdateResponse.from_dict(provider_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


