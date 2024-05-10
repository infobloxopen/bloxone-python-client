# UpdateLBDNResponse

The __LBDN__ object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**LBDN**](LBDN.md) |  | [optional] 

## Example

```python
from dns_config.models.update_lbdn_response import UpdateLBDNResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLBDNResponse from a JSON string
update_lbdn_response_instance = UpdateLBDNResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateLBDNResponse.to_json())

# convert the object into a dict
update_lbdn_response_dict = update_lbdn_response_instance.to_dict()
# create an instance of UpdateLBDNResponse from a dict
update_lbdn_response_from_dict = UpdateLBDNResponse.from_dict(update_lbdn_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


