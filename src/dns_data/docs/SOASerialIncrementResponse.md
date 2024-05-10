# SOASerialIncrementResponse

The SOA Record object serial increment response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Record**](Record.md) |  | [optional] 

## Example

```python
from dns_data.models.soa_serial_increment_response import SOASerialIncrementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SOASerialIncrementResponse from a JSON string
soa_serial_increment_response_instance = SOASerialIncrementResponse.from_json(json)
# print the JSON string representation of the object
print(SOASerialIncrementResponse.to_json())

# convert the object into a dict
soa_serial_increment_response_dict = soa_serial_increment_response_instance.to_dict()
# create an instance of SOASerialIncrementResponse from a dict
soa_serial_increment_response_from_dict = SOASerialIncrementResponse.from_dict(soa_serial_increment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


