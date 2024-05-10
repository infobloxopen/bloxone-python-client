# ListIpamHostResponse

The response format to retrieve __IpamHost__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[IpamHost]**](IpamHost.md) | The list of IpamHost objects. | [optional] 

## Example

```python
from ipam.models.list_ipam_host_response import ListIpamHostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListIpamHostResponse from a JSON string
list_ipam_host_response_instance = ListIpamHostResponse.from_json(json)
# print the JSON string representation of the object
print(ListIpamHostResponse.to_json())

# convert the object into a dict
list_ipam_host_response_dict = list_ipam_host_response_instance.to_dict()
# create an instance of ListIpamHostResponse from a dict
list_ipam_host_response_from_dict = ListIpamHostResponse.from_dict(list_ipam_host_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


