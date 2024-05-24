# RedirectPage

The Redirect Page object.  When blocking users from accessing certain domains, you can redirect them to a page that delivers a default message about the action. You can also set a redirect page of your own or customize the redirect message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The content of the redirect page for the \&quot;custom\&quot; redirect type. | [optional] 
**created_time** | **datetime** | The time when this Redirect Page object was created. | [optional] [readonly] 
**redirect_ip_address** | **str** | The redirect IPv4 address. | [optional] 
**redirect_ipv6_address** | **str** | The redirect IPv6 address. | [optional] 
**smart** | **bool** | Whether the redirect type is smart | [optional] 
**type** | **str** | The type of the redirect page that can be \&quot;default\&quot; or \&quot;custom\&quot;. | [optional] 
**updated_time** | **datetime** | The time when this Redirect Page object was last updated. | [optional] [readonly] 

## Example

```python
from redirect.models.redirect_page import RedirectPage

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectPage from a JSON string
redirect_page_instance = RedirectPage.from_json(json)
# print the JSON string representation of the object
print(RedirectPage.to_json())

# convert the object into a dict
redirect_page_dict = redirect_page_instance.to_dict()
# create an instance of RedirectPage from a dict
redirect_page_from_dict = RedirectPage.from_dict(redirect_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


