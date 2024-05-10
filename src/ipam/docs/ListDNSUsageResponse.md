# ListDNSUsageResponse

The response format to retrieve __DNSUsage__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DNSUsage]**](DNSUsage.md) | The list of DNSUsage objects. | [optional] 

## Example

```python
from ipam.models.list_dns_usage_response import ListDNSUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDNSUsageResponse from a JSON string
list_dns_usage_response_instance = ListDNSUsageResponse.from_json(json)
# print the JSON string representation of the object
print(ListDNSUsageResponse.to_json())

# convert the object into a dict
list_dns_usage_response_dict = list_dns_usage_response_instance.to_dict()
# create an instance of ListDNSUsageResponse from a dict
list_dns_usage_response_from_dict = ListDNSUsageResponse.from_dict(list_dns_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


