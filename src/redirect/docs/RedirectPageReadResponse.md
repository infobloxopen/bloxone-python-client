# RedirectPageReadResponse

The Redirect Page read response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**RedirectPage**](RedirectPage.md) | The Redirect Page object. | [optional] 

## Example

```python
from redirect.models.redirect_page_read_response import RedirectPageReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectPageReadResponse from a JSON string
redirect_page_read_response_instance = RedirectPageReadResponse.from_json(json)
# print the JSON string representation of the object
print(RedirectPageReadResponse.to_json())

# convert the object into a dict
redirect_page_read_response_dict = redirect_page_read_response_instance.to_dict()
# create an instance of RedirectPageReadResponse from a dict
redirect_page_read_response_from_dict = RedirectPageReadResponse.from_dict(redirect_page_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


