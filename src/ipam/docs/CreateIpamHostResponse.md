# CreateIpamHostResponse

The response format to create the __IpamHost__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**IpamHost**](IpamHost.md) | The created IpamHost object. | [optional] 

## Example

```python
from ipam.models.create_ipam_host_response import CreateIpamHostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIpamHostResponse from a JSON string
create_ipam_host_response_instance = CreateIpamHostResponse.from_json(json)
# print the JSON string representation of the object
print(CreateIpamHostResponse.to_json())

# convert the object into a dict
create_ipam_host_response_dict = create_ipam_host_response_instance.to_dict()
# create an instance of CreateIpamHostResponse from a dict
create_ipam_host_response_from_dict = CreateIpamHostResponse.from_dict(create_ipam_host_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


