# OptionFilterRuleList

An __OptionFilterRuleList__ object (_dhcp/option_filter_rule_list_) represents a collection of DHCP option filter rules that supports matching all or any rules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match** | **str** | Indicates if this list should match if any or all rules match (_any_ or _all_). | [optional] 
**rules** | [**List[OptionFilterRule]**](OptionFilterRule.md) | The list of child rules. | [optional] 

## Example

```python
from ipam.models.option_filter_rule_list import OptionFilterRuleList

# TODO update the JSON string below
json = "{}"
# create an instance of OptionFilterRuleList from a JSON string
option_filter_rule_list_instance = OptionFilterRuleList.from_json(json)
# print the JSON string representation of the object
print(OptionFilterRuleList.to_json())

# convert the object into a dict
option_filter_rule_list_dict = option_filter_rule_list_instance.to_dict()
# create an instance of OptionFilterRuleList from a dict
option_filter_rule_list_from_dict = OptionFilterRuleList.from_dict(option_filter_rule_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


