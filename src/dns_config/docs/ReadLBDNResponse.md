# ReadLBDNResponse

The __LBDN__ object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**LBDN**](LBDN.md) |  | [optional] 

## Example

```python
from dns_config.models.read_lbdn_response import ReadLBDNResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadLBDNResponse from a JSON string
read_lbdn_response_instance = ReadLBDNResponse.from_json(json)
# print the JSON string representation of the object
print(ReadLBDNResponse.to_json())

# convert the object into a dict
read_lbdn_response_dict = read_lbdn_response_instance.to_dict()
# create an instance of ReadLBDNResponse from a dict
read_lbdn_response_from_dict = ReadLBDNResponse.from_dict(read_lbdn_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


