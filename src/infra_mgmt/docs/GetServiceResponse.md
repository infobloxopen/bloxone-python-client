# GetServiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Service**](Service.md) |  | [optional] 

## Example

```python
from infra_mgmt.models.get_service_response import GetServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetServiceResponse from a JSON string
get_service_response_instance = GetServiceResponse.from_json(json)
# print the JSON string representation of the object
print(GetServiceResponse.to_json())

# convert the object into a dict
get_service_response_dict = get_service_response_instance.to_dict()
# create an instance of GetServiceResponse from a dict
get_service_response_from_dict = GetServiceResponse.from_dict(get_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


