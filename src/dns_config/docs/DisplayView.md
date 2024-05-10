# DisplayView

Structure containing minimal information regarding the view to be present to the UI.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | DNS view description. | [optional] [readonly] 
**name** | **str** | DNS view name. | [optional] [readonly] 
**view** | **str** | The resource identifier. | [optional] 

## Example

```python
from dns_config.models.display_view import DisplayView

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayView from a JSON string
display_view_instance = DisplayView.from_json(json)
# print the JSON string representation of the object
print(DisplayView.to_json())

# convert the object into a dict
display_view_dict = display_view_instance.to_dict()
# create an instance of DisplayView from a dict
display_view_from_dict = DisplayView.from_dict(display_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


