# DNSUsage

The __DNSUsage__ object tracks DNS usage of a resource record on an address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_name** | **str** | The absolute name of the resource record in associated zone. | [optional] [readonly] 
**address** | **str** | The address of the referenced record. | [optional] [readonly] 
**dns_rdata** | **str** | The DNS rdata of the referenced record. | [optional] [readonly] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**name** | **str** | The name in zone of the referenced record. | [optional] [readonly] 
**record** | **str** | The resource identifier. | [optional] 
**space** | **str** | The resource identifier. | [optional] 
**type** | **str** | The type of the referenced record. | [optional] [readonly] 
**view** | **str** | The resource identifier. | [optional] 
**zone** | **str** | The resource identifier. | [optional] 

## Example

```python
from ipam.models.dns_usage import DNSUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DNSUsage from a JSON string
dns_usage_instance = DNSUsage.from_json(json)
# print the JSON string representation of the object
print(DNSUsage.to_json())

# convert the object into a dict
dns_usage_dict = dns_usage_instance.to_dict()
# create an instance of DNSUsage from a dict
dns_usage_from_dict = DNSUsage.from_dict(dns_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


