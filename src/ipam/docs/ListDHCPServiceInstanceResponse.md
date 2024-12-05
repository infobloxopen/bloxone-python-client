# ListDHCPServiceInstanceResponse

The response format to retrieve DHCP __Service__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DHCPServiceInstance]**](DHCPServiceInstance.md) | The list of DHCP Service objects. | [optional] 

## Example

```python
from ipam.models.list_dhcp_service_instance_response import ListDHCPServiceInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDHCPServiceInstanceResponse from a JSON string
list_dhcp_service_instance_response_instance = ListDHCPServiceInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(ListDHCPServiceInstanceResponse.to_json())

# convert the object into a dict
list_dhcp_service_instance_response_dict = list_dhcp_service_instance_response_instance.to_dict()
# create an instance of ListDHCPServiceInstanceResponse from a dict
list_dhcp_service_instance_response_from_dict = ListDHCPServiceInstanceResponse.from_dict(list_dhcp_service_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


