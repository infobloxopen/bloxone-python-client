# CreateRangeResponse

The response format to create the __Range__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Range**](Range.md) | The created Range object. | [optional] 

## Example

```python
from ipam.models.create_range_response import CreateRangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRangeResponse from a JSON string
create_range_response_instance = CreateRangeResponse.from_json(json)
# print the JSON string representation of the object
print(CreateRangeResponse.to_json())

# convert the object into a dict
create_range_response_dict = create_range_response_instance.to_dict()
# create an instance of CreateRangeResponse from a dict
create_range_response_from_dict = CreateRangeResponse.from_dict(create_range_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


