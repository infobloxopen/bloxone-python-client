# ConvertDomainNameResponse

The ConvertDomainName object convert response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ConvertDomainName**](ConvertDomainName.md) |  | [optional] 

## Example

```python
from dns_config.models.convert_domain_name_response import ConvertDomainNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertDomainNameResponse from a JSON string
convert_domain_name_response_instance = ConvertDomainNameResponse.from_json(json)
# print the JSON string representation of the object
print(ConvertDomainNameResponse.to_json())

# convert the object into a dict
convert_domain_name_response_dict = convert_domain_name_response_instance.to_dict()
# create an instance of ConvertDomainNameResponse from a dict
convert_domain_name_response_from_dict = ConvertDomainNameResponse.from_dict(convert_domain_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


