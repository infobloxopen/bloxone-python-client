# InternalDomains

The Internal Domain List object.  The internal domain list is a transport object for reporting gathering internal domains. This feature allows users to configure bypass lists for specific DFP and ATEP groups. Bypass Lists provides the users to create ‘Internal Domains List’ objects with a name, description, and a list of domains/ip/cidr. These lists are referenced by and attached to DFP, and ATEP groups. Once attached to DFP, dfp configuration endpoints will return the values under all associated domain lists as domains.  Once attached to ATEP, atep login endpoint will return the values under all associated lists as bypass_list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **datetime** | The time when this Internal Domain lists object was created. | [optional] [readonly] 
**description** | **str** | The brief description for the internal domain lists . | [optional] 
**id** | **int** | The Internal Domain object identifier. | [optional] [readonly] 
**internal_domains** | **List[str]** | The list of internal domains, should be unique to each other and has to be read-only from the API level. | [optional] 
**is_default** | **bool** | True if name is &#39;Default Bypass Domains/CIDRs&#39; otherwise false. | [optional] 
**name** | **str** | The name of the internal domain lists. | [optional] 
**tags** | **object** | Enables tag support for resource where tags attribute contains user-defined key value pairs | [optional] 
**updated_time** | **datetime** | The time when this Internal domain lists object was last updated. | [optional] [readonly] 

## Example

```python
from fw.models.internal_domains import InternalDomains

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDomains from a JSON string
internal_domains_instance = InternalDomains.from_json(json)
# print the JSON string representation of the object
print(InternalDomains.to_json())

# convert the object into a dict
internal_domains_dict = internal_domains_instance.to_dict()
# create an instance of InternalDomains from a dict
internal_domains_from_dict = InternalDomains.from_dict(internal_domains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


