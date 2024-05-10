# ApiPageInfo

PageInfo represents both server-driven and client-driven pagination response. Server-driven pagination is a model in which the server returns some amount of data along with an token indicating there is more data and where subsequent queries can get the next page of data. Client-driven pagination is a model in which rows are addressable by offset and page size (limit).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | The service may optionally include the offset of the next page of resources. A null value indicates no more pages. | [optional] 
**page_token** | **str** | The service response should contain a string to indicate the next page of resources. A null value indicates no more pages. | [optional] 
**size** | **int** | The service may optionally include the total number of resources being paged. | [optional] 

## Example

```python
from infra_provision.models.api_page_info import ApiPageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPageInfo from a JSON string
api_page_info_instance = ApiPageInfo.from_json(json)
# print the JSON string representation of the object
print(ApiPageInfo.to_json())

# convert the object into a dict
api_page_info_dict = api_page_info_instance.to_dict()
# create an instance of ApiPageInfo from a dict
api_page_info_from_dict = ApiPageInfo.from_dict(api_page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


