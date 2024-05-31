# UpdateForwardNSGResponse

The ForwardNSG object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ForwardNSG**](ForwardNSG.md) | The updated ForwardNSG object. | [optional] 

## Example

```python
from dns_config.models.update_forward_nsg_response import UpdateForwardNSGResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateForwardNSGResponse from a JSON string
update_forward_nsg_response_instance = UpdateForwardNSGResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateForwardNSGResponse.to_json())

# convert the object into a dict
update_forward_nsg_response_dict = update_forward_nsg_response_instance.to_dict()
# create an instance of UpdateForwardNSGResponse from a dict
update_forward_nsg_response_from_dict = UpdateForwardNSGResponse.from_dict(update_forward_nsg_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


