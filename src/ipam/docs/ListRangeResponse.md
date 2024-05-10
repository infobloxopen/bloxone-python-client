# ListRangeResponse

The response format to retrieve __Range__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Range]**](Range.md) | The list of Range objects. | [optional] 

## Example

```python
from ipam.models.list_range_response import ListRangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListRangeResponse from a JSON string
list_range_response_instance = ListRangeResponse.from_json(json)
# print the JSON string representation of the object
print(ListRangeResponse.to_json())

# convert the object into a dict
list_range_response_dict = list_range_response_instance.to_dict()
# create an instance of ListRangeResponse from a dict
list_range_response_from_dict = ListRangeResponse.from_dict(list_range_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


