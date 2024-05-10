# InternalDomainsMultiResponse

The Internal domains list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[InternalDomains]**](InternalDomains.md) | The list of Internal Domains objects. | [optional] 

## Example

```python
from fw.models.internal_domains_multi_response import InternalDomainsMultiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDomainsMultiResponse from a JSON string
internal_domains_multi_response_instance = InternalDomainsMultiResponse.from_json(json)
# print the JSON string representation of the object
print(InternalDomainsMultiResponse.to_json())

# convert the object into a dict
internal_domains_multi_response_dict = internal_domains_multi_response_instance.to_dict()
# create an instance of InternalDomainsMultiResponse from a dict
internal_domains_multi_response_from_dict = InternalDomainsMultiResponse.from_dict(internal_domains_multi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


