# ReadRangeResponse

The response format to retrieve the __Range__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Range**](Range.md) |  | [optional] 

## Example

```python
from ipam.models.read_range_response import ReadRangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadRangeResponse from a JSON string
read_range_response_instance = ReadRangeResponse.from_json(json)
# print the JSON string representation of the object
print(ReadRangeResponse.to_json())

# convert the object into a dict
read_range_response_dict = read_range_response_instance.to_dict()
# create an instance of ReadRangeResponse from a dict
read_range_response_from_dict = ReadRangeResponse.from_dict(read_range_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


