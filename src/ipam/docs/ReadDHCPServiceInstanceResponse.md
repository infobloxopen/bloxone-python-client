# ReadDHCPServiceInstanceResponse

The response format to retrieve the DHCP __Service__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**DHCPServiceInstance**](DHCPServiceInstance.md) | The DHCP Service object. | [optional] 

## Example

```python
from ipam.models.read_dhcp_service_instance_response import ReadDHCPServiceInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadDHCPServiceInstanceResponse from a JSON string
read_dhcp_service_instance_response_instance = ReadDHCPServiceInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(ReadDHCPServiceInstanceResponse.to_json())

# convert the object into a dict
read_dhcp_service_instance_response_dict = read_dhcp_service_instance_response_instance.to_dict()
# create an instance of ReadDHCPServiceInstanceResponse from a dict
read_dhcp_service_instance_response_from_dict = ReadDHCPServiceInstanceResponse.from_dict(read_dhcp_service_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


