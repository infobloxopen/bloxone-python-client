# NextAvailableABResponse

The Next Available Address Block object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AddressBlock]**](AddressBlock.md) | The list of Next Available Address Block objects. | [optional] 

## Example

```python
from ipam.models.next_available_ab_response import NextAvailableABResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NextAvailableABResponse from a JSON string
next_available_ab_response_instance = NextAvailableABResponse.from_json(json)
# print the JSON string representation of the object
print(NextAvailableABResponse.to_json())

# convert the object into a dict
next_available_ab_response_dict = next_available_ab_response_instance.to_dict()
# create an instance of NextAvailableABResponse from a dict
next_available_ab_response_from_dict = NextAvailableABResponse.from_dict(next_available_ab_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


