# ServiceStatusUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**ophid** | **str** |  | [optional] 
**status_code** | [**ServiceStatusCode**](ServiceStatusCode.md) |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from anycast.models.service_status_update_request import ServiceStatusUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStatusUpdateRequest from a JSON string
service_status_update_request_instance = ServiceStatusUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceStatusUpdateRequest.to_json())

# convert the object into a dict
service_status_update_request_dict = service_status_update_request_instance.to_dict()
# create an instance of ServiceStatusUpdateRequest from a dict
service_status_update_request_from_dict = ServiceStatusUpdateRequest.from_dict(service_status_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


