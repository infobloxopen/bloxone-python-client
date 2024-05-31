# OptionFilter

An __OptionFilter__ object (_dhcp/option_filter_) applies options to DHCP clients with matching options. It must be configured in the _filters_ list for a scope to be effective.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The description for the option filter. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**dhcp_options** | [**List[OptionItem]**](OptionItem.md) | The list of DHCP options for the option filter. May be either a specific option or a group of options. | [optional] 
**header_option_filename** | **str** | The configuration for header option filename field. | [optional] 
**header_option_server_address** | **str** | The configuration for header option server address field. | [optional] 
**header_option_server_name** | **str** | The configuration for header option server name field. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**lease_time** | **int** | The lease lifetime duration in seconds. | [optional] 
**name** | **str** | The name of the option filter. Must contain 1 to 256 characters. Can include UTF-8. | 
**protocol** | **str** | The type of protocol of option filter (_ip4_ or _ip6_). | [optional] 
**role** | **str** | The role of DHCP filter (_values_ or _selection_).  Defaults to _values_. | [optional] 
**rules** | [**OptionFilterRuleList**](OptionFilterRuleList.md) | The list of option filter rules to match. | 
**tags** | **object** | The tags for the option filter in JSON format. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 
**vendor_specific_option_option_space** | **str** | The resource identifier. | [optional] 

## Example

```python
from ipam.models.option_filter import OptionFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OptionFilter from a JSON string
option_filter_instance = OptionFilter.from_json(json)
# print the JSON string representation of the object
print(OptionFilter.to_json())

# convert the object into a dict
option_filter_dict = option_filter_instance.to_dict()
# create an instance of OptionFilter from a dict
option_filter_from_dict = OptionFilter.from_dict(option_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


