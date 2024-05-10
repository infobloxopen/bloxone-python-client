# HostnameRewriteBlock

Hostname Rewrite grouping fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname_rewrite_char** | **str** | The inheritance configuration for _hostname_rewrite_char_ field. | [optional] 
**hostname_rewrite_enabled** | **bool** | The inheritance configuration for _hostname_rewrite_enabled_ field. | [optional] 
**hostname_rewrite_regex** | **str** | The inheritance configuration for _hostname_rewrite_regex_ field. | [optional] 

## Example

```python
from ipam.models.hostname_rewrite_block import HostnameRewriteBlock

# TODO update the JSON string below
json = "{}"
# create an instance of HostnameRewriteBlock from a JSON string
hostname_rewrite_block_instance = HostnameRewriteBlock.from_json(json)
# print the JSON string representation of the object
print(HostnameRewriteBlock.to_json())

# convert the object into a dict
hostname_rewrite_block_dict = hostname_rewrite_block_instance.to_dict()
# create an instance of HostnameRewriteBlock from a dict
hostname_rewrite_block_from_dict = HostnameRewriteBlock.from_dict(hostname_rewrite_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


