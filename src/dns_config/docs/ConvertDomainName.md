# ConvertDomainName

Used to convert between Internationalized Domain Name (IDN) and ASCII domain name (Punycode).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idn** | **str** | IDN domain name representation. | [optional] 
**punycode** | **str** | punycode domain name representation. | [optional] 

## Example

```python
from dns_config.models.convert_domain_name import ConvertDomainName

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertDomainName from a JSON string
convert_domain_name_instance = ConvertDomainName.from_json(json)
# print the JSON string representation of the object
print(ConvertDomainName.to_json())

# convert the object into a dict
convert_domain_name_dict = convert_domain_name_instance.to_dict()
# create an instance of ConvertDomainName from a dict
convert_domain_name_from_dict = ConvertDomainName.from_dict(convert_domain_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


