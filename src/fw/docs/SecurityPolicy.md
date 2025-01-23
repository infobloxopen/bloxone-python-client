# SecurityPolicy

The Security Policy object.  A security policy defines a set of rules and actions that you define to balance access and constraints so you can mitigate malicious attacks and provide security for your networks. When you create a new security policy, you first define a network scope to which you add networks, DNS forwarding proxies, and Infoblox Endpoint groups. Infoblox Cloud applies the security policy to all the entities that you include in the network scope. You can also include DNS forwarding proxies to which you want to apply the security policy.  After you define the network scope, you can add custom lists and category filters to the security policy. You can also specify actions for the added lists and filters, and to determine the precedence order for the entities. Depending on your subscription level, each security policy also comes with a set of predefined threat intelligence feeds and Threat Insight rules that are inherited from the default global policy. You cannot delete the inherited feeds and rules, but you can change their precedence order. For each policy you can define policy-level action (Default Action) gets applied when none of the policy rules apply/match. If an user really needs access to some blocked domain (web page) via a browser - there is a possibility to assign special bypass code(s) (Bypass Code) to any policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_codes** | **List[str]** | Access codes assigned to Security Policy | [optional] 
**created_time** | **datetime** | The time when this Security Policy object was created. | [optional] [readonly] 
**default_action** | **str** | The policy-level action gets applied when none of the policy rules apply/match. The default value for default_action is \&quot;action_allow\&quot;. | [optional] 
**default_redirect_name** | **str** | Name of the custom redirect, if the default_action is \&quot;action_redirect\&quot;. | [optional] 
**description** | **str** | The brief description for the security policy. | [optional] 
**dfp_services** | **List[str]** | The list of DNS Forwarding Proxy Services object identifiers. For Internal Use only. | [optional] 
**dfps** | **List[int]** | The list of DNS Forwarding Proxy object identifiers. | [optional] 
**ecs** | **bool** | Use ECS for handling policy | [optional] 
**id** | **int** | The Security Policy object identifier. | [optional] [readonly] 
**is_default** | **bool** | Flag that indicates whether this is a default security policy. | [optional] [readonly] 
**name** | **str** | The name of the security policy. | [optional] 
**net_address_dfps** | [**List[NetAddrDfpAssignment]**](NetAddrDfpAssignment.md) | List of DFPs associated with this policy via network address (with corresponding network address) | [optional] 
**network_lists** | **List[int]** | The list of Network Lists identifiers that represents networks that you want to protect from malicious attacks. | [optional] 
**onprem_resolve** | **bool** | Use DNS resolve on onprem side | [optional] 
**precedence** | **int** | Security precedence enable selection of the highest priority policy, in cases where a query matches multiple policies. | [optional] 
**roaming_device_groups** | **List[int]** | The list of Infoblox Endpoint groups identifiers. | [optional] 
**rules** | [**List[SecurityPolicyRule]**](SecurityPolicyRule.md) | The list of Security Policy Rules objects that represent the set of rules and actions that you define to balance access and constraints so you can mitigate malicious attacks and provide security for your networks. | [optional] 
**safe_search** | **bool** | Apply automated rules to enforce safe search | [optional] 
**tags** | **object** | Enables tag support for resource where tags attribute contains user-defined key value pairs | [optional] 
**updated_time** | **datetime** | The time when this Security Policy object was last updated. | [optional] [readonly] 
**user_groups** | **List[str]** | List of user groups associated with this policy | [optional] 

## Example

```python
from fw.models.security_policy import SecurityPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPolicy from a JSON string
security_policy_instance = SecurityPolicy.from_json(json)
# print the JSON string representation of the object
print(SecurityPolicy.to_json())

# convert the object into a dict
security_policy_dict = security_policy_instance.to_dict()
# create an instance of SecurityPolicy from a dict
security_policy_from_dict = SecurityPolicy.from_dict(security_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


