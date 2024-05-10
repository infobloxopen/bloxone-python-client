# UpdateHAGroupResponse

The response format to update the __HAGroup__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**HAGroup**](HAGroup.md) |  | [optional] 

## Example

```python
from ipam.models.update_ha_group_response import UpdateHAGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHAGroupResponse from a JSON string
update_ha_group_response_instance = UpdateHAGroupResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateHAGroupResponse.to_json())

# convert the object into a dict
update_ha_group_response_dict = update_ha_group_response_instance.to_dict()
# create an instance of UpdateHAGroupResponse from a dict
update_ha_group_response_from_dict = UpdateHAGroupResponse.from_dict(update_ha_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


