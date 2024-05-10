# DisconnectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource identifier. | [optional] [readonly] 

## Example

```python
from infra_mgmt.models.disconnect_request import DisconnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectRequest from a JSON string
disconnect_request_instance = DisconnectRequest.from_json(json)
# print the JSON string representation of the object
print(DisconnectRequest.to_json())

# convert the object into a dict
disconnect_request_dict = disconnect_request_instance.to_dict()
# create an instance of DisconnectRequest from a dict
disconnect_request_from_dict = DisconnectRequest.from_dict(disconnect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


