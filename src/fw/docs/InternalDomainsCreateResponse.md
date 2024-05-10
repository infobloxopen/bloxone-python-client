# InternalDomainsCreateResponse

The Internal Domains create response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**InternalDomains**](InternalDomains.md) |  | [optional] 

## Example

```python
from fw.models.internal_domains_create_response import InternalDomainsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDomainsCreateResponse from a JSON string
internal_domains_create_response_instance = InternalDomainsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(InternalDomainsCreateResponse.to_json())

# convert the object into a dict
internal_domains_create_response_dict = internal_domains_create_response_instance.to_dict()
# create an instance of InternalDomainsCreateResponse from a dict
internal_domains_create_response_from_dict = InternalDomainsCreateResponse.from_dict(internal_domains_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


