# UpdateRecordResponse

The response format to update the __Record__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Record**](Record.md) |  | [optional] 

## Example

```python
from dns_data.models.update_record_response import UpdateRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRecordResponse from a JSON string
update_record_response_instance = UpdateRecordResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateRecordResponse.to_json())

# convert the object into a dict
update_record_response_dict = update_record_response_instance.to_dict()
# create an instance of UpdateRecordResponse from a dict
update_record_response_from_dict = UpdateRecordResponse.from_dict(update_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


