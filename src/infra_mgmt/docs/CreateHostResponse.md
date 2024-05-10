# CreateHostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Host**](Host.md) |  | [optional] 

## Example

```python
from infra_mgmt.models.create_host_response import CreateHostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHostResponse from a JSON string
create_host_response_instance = CreateHostResponse.from_json(json)
# print the JSON string representation of the object
print(CreateHostResponse.to_json())

# convert the object into a dict
create_host_response_dict = create_host_response_instance.to_dict()
# create an instance of CreateHostResponse from a dict
create_host_response_from_dict = CreateHostResponse.from_dict(create_host_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


