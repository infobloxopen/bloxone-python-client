# OnpremHostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**OnpremHost**](OnpremHost.md) |  | [optional] 

## Example

```python
from anycast.models.onprem_host_response import OnpremHostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OnpremHostResponse from a JSON string
onprem_host_response_instance = OnpremHostResponse.from_json(json)
# print the JSON string representation of the object
print(OnpremHostResponse.to_json())

# convert the object into a dict
onprem_host_response_dict = onprem_host_response_instance.to_dict()
# create an instance of OnpremHostResponse from a dict
onprem_host_response_from_dict = OnpremHostResponse.from_dict(onprem_host_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


