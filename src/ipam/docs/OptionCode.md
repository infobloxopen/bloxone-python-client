# OptionCode

An __OptionCode__ (_dhcp/option_code_) defines a DHCP option code.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array** | **bool** | Indicates whether the option value is an array of the type or not. | [optional] 
**code** | **int** | The option code. | 
**comment** | **str** | The description for the option code. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The name of the option code. Must contain 1 to 256 characters. Can include UTF-8. | 
**option_space** | **str** | The resource identifier. | 
**source** | **str** | The source for the option code.  Valid values are:  * _dhcp_server_  * _reserved_  * _blox_one_ddi_  * _customer_  Defaults to _customer_. | [optional] [readonly] 
**type** | **str** | The option type for the option code.  Valid values are: * _address4_ * _address6_ * _boolean_ * _empty_ * _fqdn_ * _int8_ * _int16_ * _int32_ * _text_ * _uint8_ * _uint16_ * _uint32_ | 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 

## Example

```python
from ipam.models.option_code import OptionCode

# TODO update the JSON string below
json = "{}"
# create an instance of OptionCode from a JSON string
option_code_instance = OptionCode.from_json(json)
# print the JSON string representation of the object
print(OptionCode.to_json())

# convert the object into a dict
option_code_dict = option_code_instance.to_dict()
# create an instance of OptionCode from a dict
option_code_from_dict = OptionCode.from_dict(option_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


