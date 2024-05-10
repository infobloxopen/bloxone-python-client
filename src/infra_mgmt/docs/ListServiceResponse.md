# ListServiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**ApiPageInfo**](ApiPageInfo.md) |  | [optional] 
**results** | [**List[Service]**](Service.md) |  | [optional] 

## Example

```python
from infra_mgmt.models.list_service_response import ListServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListServiceResponse from a JSON string
list_service_response_instance = ListServiceResponse.from_json(json)
# print the JSON string representation of the object
print(ListServiceResponse.to_json())

# convert the object into a dict
list_service_response_dict = list_service_response_instance.to_dict()
# create an instance of ListServiceResponse from a dict
list_service_response_from_dict = ListServiceResponse.from_dict(list_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


