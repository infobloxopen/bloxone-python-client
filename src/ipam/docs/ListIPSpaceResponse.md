# ListIPSpaceResponse

The response format to retrieve __IPSpace__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[IPSpace]**](IPSpace.md) | The list of IPSpace objects. | [optional] 

## Example

```python
from ipam.models.list_ip_space_response import ListIPSpaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListIPSpaceResponse from a JSON string
list_ip_space_response_instance = ListIPSpaceResponse.from_json(json)
# print the JSON string representation of the object
print(ListIPSpaceResponse.to_json())

# convert the object into a dict
list_ip_space_response_dict = list_ip_space_response_instance.to_dict()
# create an instance of ListIPSpaceResponse from a dict
list_ip_space_response_from_dict = ListIPSpaceResponse.from_dict(list_ip_space_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


