# ListPoPRegionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PoPRegion]**](PoPRegion.md) |  | [optional] 
**total_result_count** | **int** |  | [optional] 

## Example

```python
from fw.models.list_po_p_regions_response import ListPoPRegionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPoPRegionsResponse from a JSON string
list_po_p_regions_response_instance = ListPoPRegionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListPoPRegionsResponse.to_json())

# convert the object into a dict
list_po_p_regions_response_dict = list_po_p_regions_response_instance.to_dict()
# create an instance of ListPoPRegionsResponse from a dict
list_po_p_regions_response_from_dict = ListPoPRegionsResponse.from_dict(list_po_p_regions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


