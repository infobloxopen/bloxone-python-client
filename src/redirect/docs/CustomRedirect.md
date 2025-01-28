# CustomRedirect

The Custom Redirect object.  You can configure Infoblox Cloud to redirect traffic to the Infoblox redirect page or a custom redirect destination. Infoblox Cloud allows you to apply multiple redirect actions and integrate Infoblox Cloud with third-party proxies, secure web gateways, blackholes, honeypots and sinkhole solutions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **datetime** | The time when this Custom Redirect object was created. | [optional] [readonly] 
**data** | **str** | The list of csv custom IPv4/IPv6 or a single domain redirect address. | [optional] 
**id** | **int** | The Custom Redirect object identifier. | [optional] [readonly] 
**name** | **str** | The name of the custom redirect. | [optional] 
**policy_ids** | **List[int]** | The list of the security policy identifiers with which the named list is associated. | [optional] [readonly] 
**policy_names** | **List[str]** | The list of the security policy names with which the custom redirect is associated. | [optional] [readonly] 
**updated_time** | **datetime** | The time when this Custom Redirect object was last updated. | [optional] [readonly] 

## Example

```python
from redirect.models.custom_redirect import CustomRedirect

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRedirect from a JSON string
custom_redirect_instance = CustomRedirect.from_json(json)
# print the JSON string representation of the object
print(CustomRedirect.to_json())

# convert the object into a dict
custom_redirect_dict = custom_redirect_instance.to_dict()
# create an instance of CustomRedirect from a dict
custom_redirect_from_dict = CustomRedirect.from_dict(custom_redirect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


