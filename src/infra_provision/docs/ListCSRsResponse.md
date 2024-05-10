# ListCSRsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**ApiPageInfo**](ApiPageInfo.md) |  | [optional] 
**results** | [**List[CSR]**](CSR.md) |  | [optional] 

## Example

```python
from infra_provision.models.list_csrs_response import ListCSRsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCSRsResponse from a JSON string
list_csrs_response_instance = ListCSRsResponse.from_json(json)
# print the JSON string representation of the object
print(ListCSRsResponse.to_json())

# convert the object into a dict
list_csrs_response_dict = list_csrs_response_instance.to_dict()
# create an instance of ListCSRsResponse from a dict
list_csrs_response_from_dict = ListCSRsResponse.from_dict(list_csrs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


