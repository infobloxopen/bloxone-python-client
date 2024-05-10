# DfpReadResponse

The DNS Forwarding Proxy read response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**Dfp**](Dfp.md) |  | [optional] 

## Example

```python
from dfp.models.dfp_read_response import DfpReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DfpReadResponse from a JSON string
dfp_read_response_instance = DfpReadResponse.from_json(json)
# print the JSON string representation of the object
print(DfpReadResponse.to_json())

# convert the object into a dict
dfp_read_response_dict = dfp_read_response_instance.to_dict()
# create an instance of DfpReadResponse from a dict
dfp_read_response_from_dict = DfpReadResponse.from_dict(dfp_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


