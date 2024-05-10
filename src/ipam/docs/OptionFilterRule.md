# OptionFilterRule

An __OptionFilterRule__ object (_dhcp/option_filter_rule_) represents a filter rule to match a DHCP client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compare** | **str** | Indicates how to compare the _option_value_ to the client option.  Success by comparison:  * _equals_: value and client option are the same,  * _not_equals_: value and client option are not the same,  * _exists_: client option exists,  * _not_exists_: client option does not exist,  * _text_substring_: value is the specified substring of the option,  * _not_text_substring_: value is not the specified substring of the option.  * _hex_substring_: value is the specified hexadecimal substring of the option,  * _not_hex_substring_: value is not the specified hexadecimal substring of the option. | 
**option_code** | **str** | The resource identifier. | 
**option_value** | **str** | The value to match against. | [optional] 
**substring_offset** | **int** | The offset where the substring match starts. This is used only if comparing the _option_value_ using any of the substring modes. | [optional] 

## Example

```python
from ipam.models.option_filter_rule import OptionFilterRule

# TODO update the JSON string below
json = "{}"
# create an instance of OptionFilterRule from a JSON string
option_filter_rule_instance = OptionFilterRule.from_json(json)
# print the JSON string representation of the object
print(OptionFilterRule.to_json())

# convert the object into a dict
option_filter_rule_dict = option_filter_rule_instance.to_dict()
# create an instance of OptionFilterRule from a dict
option_filter_rule_from_dict = OptionFilterRule.from_dict(option_filter_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


