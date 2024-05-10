# ApplicationsResponse

Applications response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**Applications**](Applications.md) |  | [optional] 

## Example

```python
from infra_mgmt.models.applications_response import ApplicationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsResponse from a JSON string
applications_response_instance = ApplicationsResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationsResponse.to_json())

# convert the object into a dict
applications_response_dict = applications_response_instance.to_dict()
# create an instance of ApplicationsResponse from a dict
applications_response_from_dict = ApplicationsResponse.from_dict(applications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


