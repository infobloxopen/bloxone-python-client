# CreateHAGroupResponse

The response format to create the __HAGroup__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**HAGroup**](HAGroup.md) | The created HAGroup object. | [optional] 

## Example

```python
from ipam.models.create_ha_group_response import CreateHAGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHAGroupResponse from a JSON string
create_ha_group_response_instance = CreateHAGroupResponse.from_json(json)
# print the JSON string representation of the object
print(CreateHAGroupResponse.to_json())

# convert the object into a dict
create_ha_group_response_dict = create_ha_group_response_instance.to_dict()
# create an instance of CreateHAGroupResponse from a dict
create_ha_group_response_from_dict = CreateHAGroupResponse.from_dict(create_ha_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


