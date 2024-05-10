# CreateNextAvailableIPResponse

The response format to allocate the next available IP address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Address]**](Address.md) | The list of allocated IP address objects. | [optional] 

## Example

```python
from ipam.models.create_next_available_ip_response import CreateNextAvailableIPResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNextAvailableIPResponse from a JSON string
create_next_available_ip_response_instance = CreateNextAvailableIPResponse.from_json(json)
# print the JSON string representation of the object
print(CreateNextAvailableIPResponse.to_json())

# convert the object into a dict
create_next_available_ip_response_dict = create_next_available_ip_response_instance.to_dict()
# create an instance of CreateNextAvailableIPResponse from a dict
create_next_available_ip_response_from_dict = CreateNextAvailableIPResponse.from_dict(create_next_available_ip_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


