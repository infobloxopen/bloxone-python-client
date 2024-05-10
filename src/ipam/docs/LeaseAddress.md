# LeaseAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IP address for the DHCP lease in IPv4 or IPv6 format within the IP space specified by _space_ field. | [optional] 
**space** | **str** | The resource identifier. | [optional] 

## Example

```python
from ipam.models.lease_address import LeaseAddress

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseAddress from a JSON string
lease_address_instance = LeaseAddress.from_json(json)
# print the JSON string representation of the object
print(LeaseAddress.to_json())

# convert the object into a dict
lease_address_dict = lease_address_instance.to_dict()
# create an instance of LeaseAddress from a dict
lease_address_from_dict = LeaseAddress.from_dict(lease_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


