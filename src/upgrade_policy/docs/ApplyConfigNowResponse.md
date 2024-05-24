# ApplyConfigNowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[ApplyConfigNowStatus]**](ApplyConfigNowStatus.md) |  | [optional] 

## Example

```python
from upgrade_policy.models.apply_config_now_response import ApplyConfigNowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyConfigNowResponse from a JSON string
apply_config_now_response_instance = ApplyConfigNowResponse.from_json(json)
# print the JSON string representation of the object
print(ApplyConfigNowResponse.to_json())

# convert the object into a dict
apply_config_now_response_dict = apply_config_now_response_instance.to_dict()
# create an instance of ApplyConfigNowResponse from a dict
apply_config_now_response_from_dict = ApplyConfigNowResponse.from_dict(apply_config_now_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


