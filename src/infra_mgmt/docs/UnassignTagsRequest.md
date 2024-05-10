# UnassignTagsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The resource identifier. | [optional] 
**keys** | **List[str]** |  | [optional] 

## Example

```python
from infra_mgmt.models.unassign_tags_request import UnassignTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnassignTagsRequest from a JSON string
unassign_tags_request_instance = UnassignTagsRequest.from_json(json)
# print the JSON string representation of the object
print(UnassignTagsRequest.to_json())

# convert the object into a dict
unassign_tags_request_dict = unassign_tags_request_instance.to_dict()
# create an instance of UnassignTagsRequest from a dict
unassign_tags_request_from_dict = UnassignTagsRequest.from_dict(unassign_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


