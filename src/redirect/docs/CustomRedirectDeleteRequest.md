# CustomRedirectDeleteRequest

The Custom Redirect delete request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | The list of Custom Redirect object identifiers. | [optional] 

## Example

```python
from redirect.models.custom_redirect_delete_request import CustomRedirectDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRedirectDeleteRequest from a JSON string
custom_redirect_delete_request_instance = CustomRedirectDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(CustomRedirectDeleteRequest.to_json())

# convert the object into a dict
custom_redirect_delete_request_dict = custom_redirect_delete_request_instance.to_dict()
# create an instance of CustomRedirectDeleteRequest from a dict
custom_redirect_delete_request_from_dict = CustomRedirectDeleteRequest.from_dict(custom_redirect_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


