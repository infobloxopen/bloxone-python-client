# ListDetailHostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**ApiPageInfo**](ApiPageInfo.md) |  | [optional] 
**results** | [**List[DetailHost]**](DetailHost.md) |  | [optional] 

## Example

```python
from infra_mgmt.models.list_detail_hosts_response import ListDetailHostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDetailHostsResponse from a JSON string
list_detail_hosts_response_instance = ListDetailHostsResponse.from_json(json)
# print the JSON string representation of the object
print(ListDetailHostsResponse.to_json())

# convert the object into a dict
list_detail_hosts_response_dict = list_detail_hosts_response_instance.to_dict()
# create an instance of ListDetailHostsResponse from a dict
list_detail_hosts_response_from_dict = ListDetailHostsResponse.from_dict(list_detail_hosts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


