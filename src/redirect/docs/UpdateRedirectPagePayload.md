# UpdateRedirectPagePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The content of the redirect page for the \&quot;custom\&quot; redirect type. | [optional] 
**redirect_ip_address** | **str** | The redirect IPv4 address. | [optional] 
**redirect_ipv6_address** | **str** | The redirect IPv6 address. | [optional] 
**smart** | **bool** | Change the redirect page from non-proxy (smart &#x3D;&#x3D; false) to proxy (smart) | [optional] 
**type** | **str** | The type of the redirect page that can be \&quot;default\&quot; or \&quot;custom\&quot;. | [optional] 

## Example

```python
from redirect.models.update_redirect_page_payload import UpdateRedirectPagePayload

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRedirectPagePayload from a JSON string
update_redirect_page_payload_instance = UpdateRedirectPagePayload.from_json(json)
# print the JSON string representation of the object
print(UpdateRedirectPagePayload.to_json())

# convert the object into a dict
update_redirect_page_payload_dict = update_redirect_page_payload_instance.to_dict()
# create an instance of UpdateRedirectPagePayload from a dict
update_redirect_page_payload_from_dict = UpdateRedirectPagePayload.from_dict(update_redirect_page_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


