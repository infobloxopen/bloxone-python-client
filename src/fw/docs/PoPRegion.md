# PoPRegion

PoPRegion message for a Point of Presence (PoP) region

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | PoP Region&#39;s IP addresses | [optional] 
**id** | **int** | The PoP Region&#39;s serial, unique ID | [optional] [readonly] 
**location** | **str** | PoP Region&#39;s location | [optional] 
**region** | **str** | PoP Region&#39;s name | [optional] 

## Example

```python
from fw.models.po_p_region import PoPRegion

# TODO update the JSON string below
json = "{}"
# create an instance of PoPRegion from a JSON string
po_p_region_instance = PoPRegion.from_json(json)
# print the JSON string representation of the object
print(PoPRegion.to_json())

# convert the object into a dict
po_p_region_dict = po_p_region_instance.to_dict()
# create an instance of PoPRegion from a dict
po_p_region_from_dict = PoPRegion.from_dict(po_p_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


