# InternalDomainsReadResponse

The Internal Domains read response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**InternalDomains**](InternalDomains.md) |  | [optional] 

## Example

```python
from fw.models.internal_domains_read_response import InternalDomainsReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDomainsReadResponse from a JSON string
internal_domains_read_response_instance = InternalDomainsReadResponse.from_json(json)
# print the JSON string representation of the object
print(InternalDomainsReadResponse.to_json())

# convert the object into a dict
internal_domains_read_response_dict = internal_domains_read_response_instance.to_dict()
# create an instance of InternalDomainsReadResponse from a dict
internal_domains_read_response_from_dict = InternalDomainsReadResponse.from_dict(internal_domains_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


