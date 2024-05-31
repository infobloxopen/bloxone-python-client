# RedirectPageUpdateResponse

The Redirect Page update response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**RedirectPage**](RedirectPage.md) | The Redirect Page object. | [optional] 

## Example

```python
from redirect.models.redirect_page_update_response import RedirectPageUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectPageUpdateResponse from a JSON string
redirect_page_update_response_instance = RedirectPageUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(RedirectPageUpdateResponse.to_json())

# convert the object into a dict
redirect_page_update_response_dict = redirect_page_update_response_instance.to_dict()
# create an instance of RedirectPageUpdateResponse from a dict
redirect_page_update_response_from_dict = RedirectPageUpdateResponse.from_dict(redirect_page_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


