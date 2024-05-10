# ReadPoPRegionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**PoPRegion**](PoPRegion.md) |  | [optional] 

## Example

```python
from fw.models.read_po_p_region_response import ReadPoPRegionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadPoPRegionResponse from a JSON string
read_po_p_region_response_instance = ReadPoPRegionResponse.from_json(json)
# print the JSON string representation of the object
print(ReadPoPRegionResponse.to_json())

# convert the object into a dict
read_po_p_region_response_dict = read_po_p_region_response_instance.to_dict()
# create an instance of ReadPoPRegionResponse from a dict
read_po_p_region_response_from_dict = ReadPoPRegionResponse.from_dict(read_po_p_region_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


