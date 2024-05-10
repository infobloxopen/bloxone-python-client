# UpdateIpamHostResponse

The response format to update the _IpamHost__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**IpamHost**](IpamHost.md) |  | [optional] 

## Example

```python
from ipam.models.update_ipam_host_response import UpdateIpamHostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIpamHostResponse from a JSON string
update_ipam_host_response_instance = UpdateIpamHostResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateIpamHostResponse.to_json())

# convert the object into a dict
update_ipam_host_response_dict = update_ipam_host_response_instance.to_dict()
# create an instance of UpdateIpamHostResponse from a dict
update_ipam_host_response_from_dict = UpdateIpamHostResponse.from_dict(update_ipam_host_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


