# ReplaceHostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The resource identifier. | [optional] 
**to** | **str** | The resource identifier. | [optional] 

## Example

```python
from infra_mgmt.models.replace_host_request import ReplaceHostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceHostRequest from a JSON string
replace_host_request_instance = ReplaceHostRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceHostRequest.to_json())

# convert the object into a dict
replace_host_request_dict = replace_host_request_instance.to_dict()
# create an instance of ReplaceHostRequest from a dict
replace_host_request_from_dict = ReplaceHostRequest.from_dict(replace_host_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


