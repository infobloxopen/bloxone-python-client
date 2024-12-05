# ListConfigProfileResponse

The response format to retrieve config profiles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Server]**](Server.md) | Contains result-set depending on the type. | [optional] 

## Example

```python
from ipam.models.list_config_profile_response import ListConfigProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfigProfileResponse from a JSON string
list_config_profile_response_instance = ListConfigProfileResponse.from_json(json)
# print the JSON string representation of the object
print(ListConfigProfileResponse.to_json())

# convert the object into a dict
list_config_profile_response_dict = list_config_profile_response_instance.to_dict()
# create an instance of ListConfigProfileResponse from a dict
list_config_profile_response_from_dict = ListConfigProfileResponse.from_dict(list_config_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


