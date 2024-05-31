# CustomRedirectUpdateResponse

The Custom Redirect update response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**CustomRedirect**](CustomRedirect.md) | The Custom Redirect object. | [optional] 

## Example

```python
from redirect.models.custom_redirect_update_response import CustomRedirectUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRedirectUpdateResponse from a JSON string
custom_redirect_update_response_instance = CustomRedirectUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(CustomRedirectUpdateResponse.to_json())

# convert the object into a dict
custom_redirect_update_response_dict = custom_redirect_update_response_instance.to_dict()
# create an instance of CustomRedirectUpdateResponse from a dict
custom_redirect_update_response_from_dict = CustomRedirectUpdateResponse.from_dict(custom_redirect_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


