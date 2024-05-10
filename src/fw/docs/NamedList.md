# NamedList

The Named List object.  The Named List object represents several types of lists allowed for BloxOne Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed.  Note that lists representing predefined TI feeds cannot be created, updated and deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence_level** | **str** | The confidence level for a custom list. The possible values are [\&quot;LOW\&quot;, \&quot;MEDIUM\&quot;, \&quot;HIGH\&quot;] | [optional] 
**created_time** | **datetime** | The time when this Named List object was created. | [optional] [readonly] 
**description** | **str** | The brief description for the named list. | [optional] 
**id** | **int** | The Named List object identifier. | [optional] [readonly] 
**item_count** | **int** | The number of items in this named list. | [optional] [readonly] 
**items** | **List[str]** | The list of the FQDN or IPv4/IPv6 CIDRs to define whitelists and blacklists for additional protection. | [optional] 
**items_described** | [**List[ItemStructs]**](ItemStructs.md) | The List of ItemStructs structure which contains the item and its description | [optional] 
**name** | **str** | The name of the named list. | [optional] 
**policies** | **List[str]** | The list of the security policy names with which the named list is associated. | [optional] 
**tags** | **object** | Enables tag support for resource where tags attribute contains user-defined key value pairs | [optional] 
**threat_level** | **str** | The threat level for a custom list. The possible values are [\&quot;INFO\&quot;, \&quot;LOW\&quot;, \&quot;MEDIUM\&quot;, \&quot;HIGH\&quot;] | [optional] 
**type** | **str** | The type of the named list, that can be \&quot;custom_list\&quot;, \&quot;threat_insight\&quot;, \&quot;fast_flux\&quot;, \&quot;dga\&quot;, \&quot;dnsm\&quot;, \&quot;threat_insight_nde\&quot;, \&quot;default_allow\&quot;, \&quot;default_block\&quot; or \&quot;threat_insight_nde\&quot;. | [optional] 
**updated_time** | **datetime** | The time when this Named List object was last updated. | [optional] [readonly] 

## Example

```python
from fw.models.named_list import NamedList

# TODO update the JSON string below
json = "{}"
# create an instance of NamedList from a JSON string
named_list_instance = NamedList.from_json(json)
# print the JSON string representation of the object
print(NamedList.to_json())

# convert the object into a dict
named_list_dict = named_list_instance.to_dict()
# create an instance of NamedList from a dict
named_list_from_dict = NamedList.from_dict(named_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


