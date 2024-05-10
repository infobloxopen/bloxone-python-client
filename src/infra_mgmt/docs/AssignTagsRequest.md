# AssignTagsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The resource identifier. | [optional] 
**override** | **bool** |  | [optional] 
**tags** | **object** |  | [optional] 

## Example

```python
from infra_mgmt.models.assign_tags_request import AssignTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignTagsRequest from a JSON string
assign_tags_request_instance = AssignTagsRequest.from_json(json)
# print the JSON string representation of the object
print(AssignTagsRequest.to_json())

# convert the object into a dict
assign_tags_request_dict = assign_tags_request_instance.to_dict()
# create an instance of AssignTagsRequest from a dict
assign_tags_request_from_dict = AssignTagsRequest.from_dict(assign_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


