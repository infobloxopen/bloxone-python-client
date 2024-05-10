# GetHostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Host**](Host.md) |  | [optional] 

## Example

```python
from infra_mgmt.models.get_host_response import GetHostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHostResponse from a JSON string
get_host_response_instance = GetHostResponse.from_json(json)
# print the JSON string representation of the object
print(GetHostResponse.to_json())

# convert the object into a dict
get_host_response_dict = get_host_response_instance.to_dict()
# create an instance of GetHostResponse from a dict
get_host_response_from_dict = GetHostResponse.from_dict(get_host_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


