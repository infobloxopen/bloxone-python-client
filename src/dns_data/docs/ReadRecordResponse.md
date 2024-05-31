# ReadRecordResponse

The response format to retrieve the __Record__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Record**](Record.md) | The Record object. | [optional] 

## Example

```python
from dns_data.models.read_record_response import ReadRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadRecordResponse from a JSON string
read_record_response_instance = ReadRecordResponse.from_json(json)
# print the JSON string representation of the object
print(ReadRecordResponse.to_json())

# convert the object into a dict
read_record_response_dict = read_record_response_instance.to_dict()
# create an instance of ReadRecordResponse from a dict
read_record_response_from_dict = ReadRecordResponse.from_dict(read_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


