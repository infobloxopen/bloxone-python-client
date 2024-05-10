# DfpListResponse

The DNS Forwarding Proxy list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Dfp]**](Dfp.md) | The list of DNS Forwarding Proxy objects. | [optional] 

## Example

```python
from dfp.models.dfp_list_response import DfpListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DfpListResponse from a JSON string
dfp_list_response_instance = DfpListResponse.from_json(json)
# print the JSON string representation of the object
print(DfpListResponse.to_json())

# convert the object into a dict
dfp_list_response_dict = dfp_list_response_instance.to_dict()
# create an instance of DfpListResponse from a dict
dfp_list_response_from_dict = DfpListResponse.from_dict(dfp_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


