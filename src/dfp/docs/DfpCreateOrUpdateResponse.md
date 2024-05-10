# DfpCreateOrUpdateResponse

The DNS Forwarding Proxy update response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**Dfp**](Dfp.md) |  | [optional] 

## Example

```python
from dfp.models.dfp_create_or_update_response import DfpCreateOrUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DfpCreateOrUpdateResponse from a JSON string
dfp_create_or_update_response_instance = DfpCreateOrUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(DfpCreateOrUpdateResponse.to_json())

# convert the object into a dict
dfp_create_or_update_response_dict = dfp_create_or_update_response_instance.to_dict()
# create an instance of DfpCreateOrUpdateResponse from a dict
dfp_create_or_update_response_from_dict = DfpCreateOrUpdateResponse.from_dict(dfp_create_or_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


