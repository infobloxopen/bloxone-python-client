# OptionSpace

An __OptionSpace__ object (_dhcp/option_space_) represents a set of DHCP option codes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The description for the option space. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The name of the option space. Must contain 1 to 256 characters. Can include UTF-8. | 
**protocol** | **str** | The type of protocol for the option space (_ip4_ or _ip6_). | [optional] 
**tags** | **object** | The tags for the option space in JSON format. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 

## Example

```python
from ipam.models.option_space import OptionSpace

# TODO update the JSON string below
json = "{}"
# create an instance of OptionSpace from a JSON string
option_space_instance = OptionSpace.from_json(json)
# print the JSON string representation of the object
print(OptionSpace.to_json())

# convert the object into a dict
option_space_dict = option_space_instance.to_dict()
# create an instance of OptionSpace from a dict
option_space_from_dict = OptionSpace.from_dict(option_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


