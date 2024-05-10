# LeasesCommand

The __LeasesCommand__ (_dhcp/leases_command_) is used to perform an action on a lease or a set of leases defined by the list of IP addresses or Subnet or Range. Host(s) owning the lease(s) must be available for this action to succeed. The command is executed asynchronously.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**List[LeaseAddress]**](LeaseAddress.md) | The list of IP addresses to execute the \&quot;command\&quot; on. It can be 1 or more IP addresses. | [optional] 
**command** | **str** | The command to perform on the lease(s).  Valid values are:  | command       | description | | :------       | ----------- | | _clear_       | Removes selected lease(s) from the DHCP server(s). This will NOT affect the client that issued the lease. | | _resend-ddns_ | Resends a request to kea-dhcp-ddns to update DNS for selected lease(s). | | 
**range** | [**List[LeaseRange]**](LeaseRange.md) | The list of ranges to execute the \&quot;command\&quot; on. For now it is limited to 1 range. | [optional] 
**subnet** | [**List[LeaseSubnet]**](LeaseSubnet.md) | The list of subnets to execute the \&quot;command\&quot; on. For now it is limited to 1 subnet. | [optional] 

## Example

```python
from ipam.models.leases_command import LeasesCommand

# TODO update the JSON string below
json = "{}"
# create an instance of LeasesCommand from a JSON string
leases_command_instance = LeasesCommand.from_json(json)
# print the JSON string representation of the object
print(LeasesCommand.to_json())

# convert the object into a dict
leases_command_dict = leases_command_instance.to_dict()
# create an instance of LeasesCommand from a dict
leases_command_from_dict = LeasesCommand.from_dict(leases_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


