# CustomRedirectMultiResponse

The Custom Redirect list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CustomRedirect]**](CustomRedirect.md) | The list of Custom Redirect objects. | [optional] 

## Example

```python
from redirect.models.custom_redirect_multi_response import CustomRedirectMultiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRedirectMultiResponse from a JSON string
custom_redirect_multi_response_instance = CustomRedirectMultiResponse.from_json(json)
# print the JSON string representation of the object
print(CustomRedirectMultiResponse.to_json())

# convert the object into a dict
custom_redirect_multi_response_dict = custom_redirect_multi_response_instance.to_dict()
# create an instance of CustomRedirectMultiResponse from a dict
custom_redirect_multi_response_from_dict = CustomRedirectMultiResponse.from_dict(custom_redirect_multi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


