# ListHAGroupResponse

The response format to retrieve __HAGroup__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[HAGroup]**](HAGroup.md) | The list of HAGroup objects. | [optional] 

## Example

```python
from ipam.models.list_ha_group_response import ListHAGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListHAGroupResponse from a JSON string
list_ha_group_response_instance = ListHAGroupResponse.from_json(json)
# print the JSON string representation of the object
print(ListHAGroupResponse.to_json())

# convert the object into a dict
list_ha_group_response_dict = list_ha_group_response_instance.to_dict()
# create an instance of ListHAGroupResponse from a dict
list_ha_group_response_from_dict = ListHAGroupResponse.from_dict(list_ha_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


