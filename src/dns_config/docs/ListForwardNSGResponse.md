# ListForwardNSGResponse

The ForwardNSG object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ForwardNSG]**](ForwardNSG.md) | List of ForwardNSG objects. | [optional] 

## Example

```python
from dns_config.models.list_forward_nsg_response import ListForwardNSGResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListForwardNSGResponse from a JSON string
list_forward_nsg_response_instance = ListForwardNSGResponse.from_json(json)
# print the JSON string representation of the object
print(ListForwardNSGResponse.to_json())

# convert the object into a dict
list_forward_nsg_response_dict = list_forward_nsg_response_instance.to_dict()
# create an instance of ListForwardNSGResponse from a dict
list_forward_nsg_response_from_dict = ListForwardNSGResponse.from_dict(list_forward_nsg_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


