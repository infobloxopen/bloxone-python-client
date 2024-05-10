# CreateViewResponse

The View object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**View**](View.md) |  | [optional] 

## Example

```python
from dns_config.models.create_view_response import CreateViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateViewResponse from a JSON string
create_view_response_instance = CreateViewResponse.from_json(json)
# print the JSON string representation of the object
print(CreateViewResponse.to_json())

# convert the object into a dict
create_view_response_dict = create_view_response_instance.to_dict()
# create an instance of CreateViewResponse from a dict
create_view_response_from_dict = CreateViewResponse.from_dict(create_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


