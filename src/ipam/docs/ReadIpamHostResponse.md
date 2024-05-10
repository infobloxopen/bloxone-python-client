# ReadIpamHostResponse

The response format to retrieve the __IpamHost__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**IpamHost**](IpamHost.md) |  | [optional] 

## Example

```python
from ipam.models.read_ipam_host_response import ReadIpamHostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadIpamHostResponse from a JSON string
read_ipam_host_response_instance = ReadIpamHostResponse.from_json(json)
# print the JSON string representation of the object
print(ReadIpamHostResponse.to_json())

# convert the object into a dict
read_ipam_host_response_dict = read_ipam_host_response_instance.to_dict()
# create an instance of ReadIpamHostResponse from a dict
read_ipam_host_response_from_dict = ReadIpamHostResponse.from_dict(read_ipam_host_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


