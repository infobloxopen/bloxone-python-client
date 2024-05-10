# SOASerialIncrementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**ProtobufFieldMask**](ProtobufFieldMask.md) |  | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**serial_increment** | **int** | Default increment SOA serial number by 1,000. | [optional] 

## Example

```python
from dns_data.models.soa_serial_increment_request import SOASerialIncrementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SOASerialIncrementRequest from a JSON string
soa_serial_increment_request_instance = SOASerialIncrementRequest.from_json(json)
# print the JSON string representation of the object
print(SOASerialIncrementRequest.to_json())

# convert the object into a dict
soa_serial_increment_request_dict = soa_serial_increment_request_instance.to_dict()
# create an instance of SOASerialIncrementRequest from a dict
soa_serial_increment_request_from_dict = SOASerialIncrementRequest.from_dict(soa_serial_increment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


