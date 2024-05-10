# ForwardersBlock

Block for fields: _forwarders_, _forwarders_only_, _use_root_forwarders_for_local_resolution_with_b1td_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarders** | [**List[Forwarder]**](Forwarder.md) | Optional. Field config for _forwarders_ field from. | [optional] 
**forwarders_only** | **bool** | Optional. Field config for _forwarders_only_ field. | [optional] 
**use_root_forwarders_for_local_resolution_with_b1td** | **bool** | Optional. Field config for _use_root_forwarders_for_local_resolution_with_b1td_ field. | [optional] 

## Example

```python
from dns_config.models.forwarders_block import ForwardersBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardersBlock from a JSON string
forwarders_block_instance = ForwardersBlock.from_json(json)
# print the JSON string representation of the object
print(ForwardersBlock.to_json())

# convert the object into a dict
forwarders_block_dict = forwarders_block_instance.to_dict()
# create an instance of ForwardersBlock from a dict
forwarders_block_from_dict = ForwardersBlock.from_dict(forwarders_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


