# CreateLBDNResponse

The __LBDN__ object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**LBDN**](LBDN.md) | The created __LBDN__ object. | [optional] 

## Example

```python
from dns_config.models.create_lbdn_response import CreateLBDNResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLBDNResponse from a JSON string
create_lbdn_response_instance = CreateLBDNResponse.from_json(json)
# print the JSON string representation of the object
print(CreateLBDNResponse.to_json())

# convert the object into a dict
create_lbdn_response_dict = create_lbdn_response_instance.to_dict()
# create an instance of CreateLBDNResponse from a dict
create_lbdn_response_from_dict = CreateLBDNResponse.from_dict(create_lbdn_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


