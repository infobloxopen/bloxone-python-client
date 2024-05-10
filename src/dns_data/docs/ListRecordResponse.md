# ListRecordResponse

The response format to retrieve __Record__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Record]**](Record.md) | The list of Record objects. | [optional] 

## Example

```python
from dns_data.models.list_record_response import ListRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListRecordResponse from a JSON string
list_record_response_instance = ListRecordResponse.from_json(json)
# print the JSON string representation of the object
print(ListRecordResponse.to_json())

# convert the object into a dict
list_record_response_dict = list_record_response_instance.to_dict()
# create an instance of ListRecordResponse from a dict
list_record_response_from_dict = ListRecordResponse.from_dict(list_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


