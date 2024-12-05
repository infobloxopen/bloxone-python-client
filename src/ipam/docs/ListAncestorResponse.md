# ListAncestorResponse

The response format to retrieve the __AddressBlock__ objects that are ancestors of the __AddressBlock__ or __subnet__ object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CidrBlock]**](CidrBlock.md) | The list of the ancestors of the CidrBlock. | [optional] 

## Example

```python
from ipam.models.list_ancestor_response import ListAncestorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAncestorResponse from a JSON string
list_ancestor_response_instance = ListAncestorResponse.from_json(json)
# print the JSON string representation of the object
print(ListAncestorResponse.to_json())

# convert the object into a dict
list_ancestor_response_dict = list_ancestor_response_instance.to_dict()
# create an instance of ListAncestorResponse from a dict
list_ancestor_response_from_dict = ListAncestorResponse.from_dict(list_ancestor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


