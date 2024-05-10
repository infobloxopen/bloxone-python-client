# CreateLeasesCommandResponse

The response format to perform leases command.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **str** |  | [optional] 

## Example

```python
from ipam.models.create_leases_command_response import CreateLeasesCommandResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLeasesCommandResponse from a JSON string
create_leases_command_response_instance = CreateLeasesCommandResponse.from_json(json)
# print the JSON string representation of the object
print(CreateLeasesCommandResponse.to_json())

# convert the object into a dict
create_leases_command_response_dict = create_leases_command_response_instance.to_dict()
# create an instance of CreateLeasesCommandResponse from a dict
create_leases_command_response_from_dict = CreateLeasesCommandResponse.from_dict(create_leases_command_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


