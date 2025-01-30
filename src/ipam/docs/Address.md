# Address

An __Address__ object (_ipam/address_) represents any single IP address within a given IP space.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address in form \&quot;a.b.c.d\&quot;. | [optional]
**comment** | **str** | The description for the address object. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**compartment_id** | **str** | The compartment associated with the object. If no compartment is associated with the object, the value defaults to empty. | [optional] [readonly] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**dhcp_info** | [**DHCPInfo**](DHCPInfo.md) | The DHCP information associated with this object. | [optional] [readonly] 
**disable_dhcp** | **bool** | Read only. Represent the value of the same field in the associated _dhcp/fixed_address_ object. | [optional] [readonly] 
**discovery_attrs** | **object** | The discovery attributes for this address in JSON format. | [optional] [readonly] 
**discovery_metadata** | **object** | The discovery metadata for this address in JSON format. | [optional] [readonly] 
**external_keys** | **object** | The external keys (source key) for this address in JSON format. | [optional] 
**host** | **str** | The resource identifier. | [optional] 
**hwaddr** | **str** | The hardware address associated with this IP address. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**interface** | **str** | The name of the network interface card (NIC) associated with the address, if any. | [optional] 
**names** | [**List[Name]**](Name.md) | The list of all names associated with this address. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**protocol** | **str** | The type of protocol (_ip4_ or _ip6_). | [optional] [readonly] 
**range** | **str** | The resource identifier. | [optional] 
**space** | **str** | The resource identifier. | [optional] 
**state** | **str** | The state of the address (_used_ or _free_). | [optional] [readonly] 
**tags** | **object** | The tags for this address in JSON format. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 
**usage** | **List[str]** | The usage is a combination of indicators, each tracking a specific associated use. Listed below are usage indicators with their meaning:  usage indicator        | description  ---------------------- | --------------------------------  _IPAM_                 |  Address was created by the IPAM component.  _IPAM_, _RESERVED_     |  Address was created by the API call _ipam/address_ or _ipam/host_.  _IPAM_, _NETWORK_      |  Address was automatically created by the IPAM component and is the network address of the parent subnet.  _IPAM_, _BROADCAST_    |  Address was automatically created by the IPAM component and is the broadcast address of the parent subnet.  _DHCP_                 |  Address was created by the DHCP component.  _DHCP_, _FIXEDADDRESS_ |  Address was created by the API call _dhcp/fixed_address_.  _DHCP_, _LEASED_       |  An active lease for that address was issued by a DHCP server.  _DHCP_, _DISABLED_     |  Address is disabled.  _DNS_                  |  Address is used by one or more DNS records.  _DISCOVERED_           |  Address is discovered by some network discovery probe like Network Insight or NetMRI in NIOS. | [optional] [readonly] 

## Example

```python
from ipam.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


