# UpdateServiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Service**](Service.md) |  | [optional] 

## Example

```python
from infra_mgmt.models.update_service_response import UpdateServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServiceResponse from a JSON string
update_service_response_instance = UpdateServiceResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateServiceResponse.to_json())

# convert the object into a dict
update_service_response_dict = update_service_response_instance.to_dict()
# create an instance of UpdateServiceResponse from a dict
update_service_response_from_dict = UpdateServiceResponse.from_dict(update_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


