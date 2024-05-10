# DetailLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **object** | The address of the Location containing address, postal_code, city, state, and country. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**latitude** | **float** | Latitude of the Location. | [optional] 
**longitude** | **float** | Longitude of the Location. | [optional] 
**metadata** | **object** | The metadata of the Location which could contain other info such as attributions. | [optional] 

## Example

```python
from infra_mgmt.models.detail_location import DetailLocation

# TODO update the JSON string below
json = "{}"
# create an instance of DetailLocation from a JSON string
detail_location_instance = DetailLocation.from_json(json)
# print the JSON string representation of the object
print(DetailLocation.to_json())

# convert the object into a dict
detail_location_dict = detail_location_instance.to_dict()
# create an instance of DetailLocation from a dict
detail_location_from_dict = DetailLocation.from_dict(detail_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


