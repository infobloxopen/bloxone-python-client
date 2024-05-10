# ListDetailServicesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**ApiPageInfo**](ApiPageInfo.md) |  | [optional] 
**results** | [**List[DetailService]**](DetailService.md) |  | [optional] 

## Example

```python
from infra_mgmt.models.list_detail_services_response import ListDetailServicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDetailServicesResponse from a JSON string
list_detail_services_response_instance = ListDetailServicesResponse.from_json(json)
# print the JSON string representation of the object
print(ListDetailServicesResponse.to_json())

# convert the object into a dict
list_detail_services_response_dict = list_detail_services_response_instance.to_dict()
# create an instance of ListDetailServicesResponse from a dict
list_detail_services_response_from_dict = ListDetailServicesResponse.from_dict(list_detail_services_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


