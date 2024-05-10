# InternalDomainsDeleteRequest

The Internal Domains delete request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | The list of InternalDomains object identifiers. | [optional] 

## Example

```python
from fw.models.internal_domains_delete_request import InternalDomainsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDomainsDeleteRequest from a JSON string
internal_domains_delete_request_instance = InternalDomainsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(InternalDomainsDeleteRequest.to_json())

# convert the object into a dict
internal_domains_delete_request_dict = internal_domains_delete_request_instance.to_dict()
# create an instance of InternalDomainsDeleteRequest from a dict
internal_domains_delete_request_from_dict = InternalDomainsDeleteRequest.from_dict(internal_domains_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


