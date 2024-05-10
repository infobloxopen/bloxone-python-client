# DDNSHostnameBlock

The dynamic DNS Hostname configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ddns_generate_name** | **bool** | Indicates if DDNS should generate a hostname when not supplied by the client. | [optional] 
**ddns_generated_prefix** | **str** | The prefix used in the generation of an FQDN. | [optional] 

## Example

```python
from ipam.models.ddns_hostname_block import DDNSHostnameBlock

# TODO update the JSON string below
json = "{}"
# create an instance of DDNSHostnameBlock from a JSON string
ddns_hostname_block_instance = DDNSHostnameBlock.from_json(json)
# print the JSON string representation of the object
print(DDNSHostnameBlock.to_json())

# convert the object into a dict
ddns_hostname_block_dict = ddns_hostname_block_instance.to_dict()
# create an instance of DDNSHostnameBlock from a dict
ddns_hostname_block_from_dict = DDNSHostnameBlock.from_dict(ddns_hostname_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


