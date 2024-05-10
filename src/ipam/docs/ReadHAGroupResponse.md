# ReadHAGroupResponse

The response format to retrieve the __HAGroup__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**HAGroup**](HAGroup.md) |  | [optional] 

## Example

```python
from ipam.models.read_ha_group_response import ReadHAGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadHAGroupResponse from a JSON string
read_ha_group_response_instance = ReadHAGroupResponse.from_json(json)
# print the JSON string representation of the object
print(ReadHAGroupResponse.to_json())

# convert the object into a dict
read_ha_group_response_dict = read_ha_group_response_instance.to_dict()
# create an instance of ReadHAGroupResponse from a dict
read_ha_group_response_from_dict = ReadHAGroupResponse.from_dict(read_ha_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


