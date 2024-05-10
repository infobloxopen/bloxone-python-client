# DfpHost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy_host_id** | **int** | // The DNS Forwarding Proxy legacy ID object identifier. | [optional] 
**name** | **str** | The name of the DNS Forwarding Proxy. | [optional] [readonly] 
**ophid** | **str** | The On-Prem Host identifier. | [optional] [readonly] 
**site_id** | **str** | The DNS Forwarding Proxy site identifier that is appended to DNS queries originating from this DNS Forwarding Proxy and subsequently used for policy lookup purposes. | [optional] [readonly] 

## Example

```python
from dfp.models.dfp_host import DfpHost

# TODO update the JSON string below
json = "{}"
# create an instance of DfpHost from a JSON string
dfp_host_instance = DfpHost.from_json(json)
# print the JSON string representation of the object
print(DfpHost.to_json())

# convert the object into a dict
dfp_host_dict = dfp_host_instance.to_dict()
# create an instance of DfpHost from a dict
dfp_host_from_dict = DfpHost.from_dict(dfp_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


