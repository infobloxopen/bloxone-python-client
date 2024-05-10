# ReadDNSUsageResponse

The response format to retrieve the __DNSUsage__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**DNSUsage**](DNSUsage.md) |  | [optional] 

## Example

```python
from ipam.models.read_dns_usage_response import ReadDNSUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadDNSUsageResponse from a JSON string
read_dns_usage_response_instance = ReadDNSUsageResponse.from_json(json)
# print the JSON string representation of the object
print(ReadDNSUsageResponse.to_json())

# convert the object into a dict
read_dns_usage_response_dict = read_dns_usage_response_instance.to_dict()
# create an instance of ReadDNSUsageResponse from a dict
read_dns_usage_response_from_dict = ReadDNSUsageResponse.from_dict(read_dns_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


