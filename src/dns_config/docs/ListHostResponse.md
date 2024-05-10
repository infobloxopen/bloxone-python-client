# ListHostResponse

The DNS Host object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Host]**](Host.md) | List of DNS Host objects. | [optional] 

## Example

```python
from dns_config.models.list_host_response import ListHostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListHostResponse from a JSON string
list_host_response_instance = ListHostResponse.from_json(json)
# print the JSON string representation of the object
print(ListHostResponse.to_json())

# convert the object into a dict
list_host_response_dict = list_host_response_instance.to_dict()
# create an instance of ListHostResponse from a dict
list_host_response_from_dict = ListHostResponse.from_dict(list_host_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


