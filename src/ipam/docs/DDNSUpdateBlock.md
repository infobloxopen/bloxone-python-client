# DDNSUpdateBlock

The dynamic DNS configurations, ddns_domain and ddns_send_updates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ddns_domain** | **str** | The domain name for DDNS. | [optional] 
**ddns_send_updates** | **bool** | Determines if DDNS updates are enabled at this level. | [optional] 

## Example

```python
from ipam.models.ddns_update_block import DDNSUpdateBlock

# TODO update the JSON string below
json = "{}"
# create an instance of DDNSUpdateBlock from a JSON string
ddns_update_block_instance = DDNSUpdateBlock.from_json(json)
# print the JSON string representation of the object
print(DDNSUpdateBlock.to_json())

# convert the object into a dict
ddns_update_block_dict = ddns_update_block_instance.to_dict()
# create an instance of DDNSUpdateBlock from a dict
ddns_update_block_from_dict = DDNSUpdateBlock.from_dict(ddns_update_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


