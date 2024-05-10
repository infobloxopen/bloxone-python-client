# CreateForwardNSGResponse

The ForwardNSG object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ForwardNSG**](ForwardNSG.md) |  | [optional] 

## Example

```python
from dns_config.models.create_forward_nsg_response import CreateForwardNSGResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateForwardNSGResponse from a JSON string
create_forward_nsg_response_instance = CreateForwardNSGResponse.from_json(json)
# print the JSON string representation of the object
print(CreateForwardNSGResponse.to_json())

# convert the object into a dict
create_forward_nsg_response_dict = create_forward_nsg_response_instance.to_dict()
# create an instance of CreateForwardNSGResponse from a dict
create_forward_nsg_response_from_dict = CreateForwardNSGResponse.from_dict(create_forward_nsg_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


