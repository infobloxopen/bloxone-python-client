# ReadForwardNSGResponse

The ForwardNSG object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ForwardNSG**](ForwardNSG.md) |  | [optional] 

## Example

```python
from dns_config.models.read_forward_nsg_response import ReadForwardNSGResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadForwardNSGResponse from a JSON string
read_forward_nsg_response_instance = ReadForwardNSGResponse.from_json(json)
# print the JSON string representation of the object
print(ReadForwardNSGResponse.to_json())

# convert the object into a dict
read_forward_nsg_response_dict = read_forward_nsg_response_instance.to_dict()
# create an instance of ReadForwardNSGResponse from a dict
read_forward_nsg_response_from_dict = ReadForwardNSGResponse.from_dict(read_forward_nsg_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


