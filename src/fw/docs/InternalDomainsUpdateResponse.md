# InternalDomainsUpdateResponse

The Internal domains update response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**InternalDomains**](InternalDomains.md) |  | [optional] 

## Example

```python
from fw.models.internal_domains_update_response import InternalDomainsUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDomainsUpdateResponse from a JSON string
internal_domains_update_response_instance = InternalDomainsUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(InternalDomainsUpdateResponse.to_json())

# convert the object into a dict
internal_domains_update_response_dict = internal_domains_update_response_instance.to_dict()
# create an instance of InternalDomainsUpdateResponse from a dict
internal_domains_update_response_from_dict = InternalDomainsUpdateResponse.from_dict(internal_domains_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


