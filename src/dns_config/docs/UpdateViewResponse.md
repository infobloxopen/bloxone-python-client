# UpdateViewResponse

The View object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**View**](View.md) | The View object. | [optional] 

## Example

```python
from dns_config.models.update_view_response import UpdateViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateViewResponse from a JSON string
update_view_response_instance = UpdateViewResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateViewResponse.to_json())

# convert the object into a dict
update_view_response_dict = update_view_response_instance.to_dict()
# create an instance of UpdateViewResponse from a dict
update_view_response_from_dict = UpdateViewResponse.from_dict(update_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


