# IpamHost

The __IpamHost__ object (_ipam/host_) represents any network connected equipment that is assigned one or more IP addresses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**List[HostAddress]**](HostAddress.md) | The list of all addresses associated with the IPAM host, which may be in different IP spaces. | [optional] 
**auto_generate_records** | **bool** | This flag specifies if resource records have to be auto generated for the host. | [optional] 
**comment** | **str** | The description for the IPAM host. May contain 0 to 1024 characters. Can include UTF-8. | [optional] 
**created_at** | **datetime** | Time when the object has been created. | [optional] [readonly] 
**host_names** | [**List[HostName]**](HostName.md) | The name records to be generated for the host.  This field is required if _auto_generate_records_ is true. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The name of the IPAM host. Must contain 1 to 256 characters. Can include UTF-8. | 
**tags** | **object** | The tags for the IPAM host in JSON format. | [optional] 
**updated_at** | **datetime** | Time when the object has been updated. Equals to _created_at_ if not updated after creation. | [optional] [readonly] 

## Example

```python
from ipam.models.ipam_host import IpamHost

# TODO update the JSON string below
json = "{}"
# create an instance of IpamHost from a JSON string
ipam_host_instance = IpamHost.from_json(json)
# print the JSON string representation of the object
print(IpamHost.to_json())

# convert the object into a dict
ipam_host_dict = ipam_host_instance.to_dict()
# create an instance of IpamHost from a dict
ipam_host_from_dict = IpamHost.from_dict(ipam_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


