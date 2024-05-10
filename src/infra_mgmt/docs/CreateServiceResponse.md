# CreateServiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Service**](Service.md) |  | [optional] 

## Example

```python
from infra_mgmt.models.create_service_response import CreateServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServiceResponse from a JSON string
create_service_response_instance = CreateServiceResponse.from_json(json)
# print the JSON string representation of the object
print(CreateServiceResponse.to_json())

# convert the object into a dict
create_service_response_dict = create_service_response_instance.to_dict()
# create an instance of CreateServiceResponse from a dict
create_service_response_from_dict = CreateServiceResponse.from_dict(create_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


