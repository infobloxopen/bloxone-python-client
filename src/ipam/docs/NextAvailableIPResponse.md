# NextAvailableIPResponse

The response format to retrieve the next available IP address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Address]**](Address.md) | The list of next available IP address objects. | [optional] 

## Example

```python
from ipam.models.next_available_ip_response import NextAvailableIPResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NextAvailableIPResponse from a JSON string
next_available_ip_response_instance = NextAvailableIPResponse.from_json(json)
# print the JSON string representation of the object
print(NextAvailableIPResponse.to_json())

# convert the object into a dict
next_available_ip_response_dict = next_available_ip_response_instance.to_dict()
# create an instance of NextAvailableIPResponse from a dict
next_available_ip_response_from_dict = NextAvailableIPResponse.from_dict(next_available_ip_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


