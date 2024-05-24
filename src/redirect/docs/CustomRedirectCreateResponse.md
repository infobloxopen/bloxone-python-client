# CustomRedirectCreateResponse

The Custom Redirect create response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**CustomRedirect**](CustomRedirect.md) |  | [optional] 

## Example

```python
from redirect.models.custom_redirect_create_response import CustomRedirectCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRedirectCreateResponse from a JSON string
custom_redirect_create_response_instance = CustomRedirectCreateResponse.from_json(json)
# print the JSON string representation of the object
print(CustomRedirectCreateResponse.to_json())

# convert the object into a dict
custom_redirect_create_response_dict = custom_redirect_create_response_instance.to_dict()
# create an instance of CustomRedirectCreateResponse from a dict
custom_redirect_create_response_from_dict = CustomRedirectCreateResponse.from_dict(custom_redirect_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


