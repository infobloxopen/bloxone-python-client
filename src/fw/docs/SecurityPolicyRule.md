# SecurityPolicyRule

The Security Policy Rule object.  The Security Policy Rule object represents a rule and action that you define to balance access and constraints so you can mitigate malicious attacks and provide security for your networks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action for the policy rule that can be either \&quot;action_allow\&quot; or \&quot;action_log\&quot; or \&quot;action_redirect\&quot; or \&quot;action_block\&quot; or \&quot;action_allow_with_local_resolution\&quot;. \&quot;action_allow_with_local_resolution\&quot; only supported for application filter rule with enabled onprem_resolve flag on the Security policy. | [optional] 
**data** | **str** | The data source for the policy rule, that can be either a name of the predefined feed for \&quot;named_feed\&quot;, custom list name for \&quot;custom_list\&quot; type, category filter name for \&quot;category_filter\&quot; type and application filter name for \&quot;application_filter\&quot; type. | [optional] 
**list_id** | **int** | The Custom List object identifier with which the policy rule is associated. 0 value means no custom list is associated with this policy rule. | [optional] [readonly] 
**policy_id** | **int** | The identifier of the Security Policy object with which the policy rule is associated. | [optional] [readonly] 
**policy_name** | **str** | The name of the security policy with which the policy rule is associated. | [optional] 
**redirect_name** | **str** | The name of the redirect address for redirect actions that can be either IPv4 address or a domain name. | [optional] 
**type** | **str** | The policy rule type that can be either \&quot;named_feed\&quot; or \&quot;custom_list\&quot; or \&quot;category_filter\&quot; or \&quot;application_filter\&quot;. | [optional] 

## Example

```python
from fw.models.security_policy_rule import SecurityPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPolicyRule from a JSON string
security_policy_rule_instance = SecurityPolicyRule.from_json(json)
# print the JSON string representation of the object
print(SecurityPolicyRule.to_json())

# convert the object into a dict
security_policy_rule_dict = security_policy_rule_instance.to_dict()
# create an instance of SecurityPolicyRule from a dict
security_policy_rule_from_dict = SecurityPolicyRule.from_dict(security_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


