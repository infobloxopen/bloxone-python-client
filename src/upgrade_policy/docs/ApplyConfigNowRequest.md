# ApplyConfigNowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | [**List[OnpremDetails]**](OnpremDetails.md) |  | [optional] 

## Example

```python
from upgrade_policy.models.apply_config_now_request import ApplyConfigNowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyConfigNowRequest from a JSON string
apply_config_now_request_instance = ApplyConfigNowRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyConfigNowRequest.to_json())

# convert the object into a dict
apply_config_now_request_dict = apply_config_now_request_instance.to_dict()
# create an instance of ApplyConfigNowRequest from a dict
apply_config_now_request_from_dict = ApplyConfigNowRequest.from_dict(apply_config_now_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


