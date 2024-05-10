# CreateNextAvailableABResponse

The Next Available Address Block object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AddressBlock]**](AddressBlock.md) | The list of Next Available Address Block objects. | [optional] 

## Example

```python
from ipam.models.create_next_available_ab_response import CreateNextAvailableABResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNextAvailableABResponse from a JSON string
create_next_available_ab_response_instance = CreateNextAvailableABResponse.from_json(json)
# print the JSON string representation of the object
print(CreateNextAvailableABResponse.to_json())

# convert the object into a dict
create_next_available_ab_response_dict = create_next_available_ab_response_instance.to_dict()
# create an instance of CreateNextAvailableABResponse from a dict
create_next_available_ab_response_from_dict = CreateNextAvailableABResponse.from_dict(create_next_available_ab_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


